from pymongo import MongoClient
import requests
import os

'''ALWAYS set api as an os variable'''
apikey = os.environ.get('NYT_API_KEY')
#starts us the mongo server on the computer
client = MongoClient()
#creates or connects to existing database
db = client['nytimes']
#creates or connects to existing collection in the database
tab = db['articles']

#test = {"spirit animal": "goat", "name":"sky", "shoe_size": 17}
#tab.update({"name":"Andy"}, test, True)
#tab.update({"name":"sky"}, {"$set": {"shoe_size":12}}, True)

def insert_one_doc(doc_dict):
    tab.insert_one(doc_dict)

def single_query(endpoint, payload):
    response = requests.get(endpoint, params=payload)
    if response.status_code != 200:
        print('WARNING'), response.status_code
    else:
        return response.json()

if __name__ == '__main__':
    endpoint = 'http://api.nytimes.com/svc/search/v2/articlesearch.json'
    payload = {'api-key': apikey}
    response = single_query(endpoint, payload)

    '''exploration to determine where data was in the response'''
#    print(type(response['response']['docs'][0]))
#    print(response['response']['docs'][0])

    '''exactly where to key into changes with each data source'''
    for doc in response['response']['docs']:
        insert_one_doc(doc)
