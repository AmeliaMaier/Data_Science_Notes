
import psycopg2
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
import os

mysql_user = os.environ.get('mysql_USER')
mysql_password = os.environ.get('mysql_PASSWORD')
mysql_port = os.environ.get('mysql_PORT')
mysql_host = os.environ.get('mysql_HOST')
mysql_db = os.environ.get('mysql_DB')
psql_user = os.environ.get('PSQL_USER')
psql_password = os.environ.get('PSQL_PASSWORD')

print('attempting to connect to mysql')
sql_cnx = mysql.connector.connect(user=mysql_user, password=mysql_password, port=mysql_port,
                              host=mysql_host,
                              database=mysql_db)


tables = ["list of table names"]



#print('attempting to read tables')
for table in tables:
    #read table from trackwell to dataframe
   # print(f'reading table {table}')
    df = pd.read_sql(f'SELECT * FROM {table}', con=sql_cnx)
    #write dataframe to local psql database
   # print(f'writing table {table} with {df.info()}')
    engine = create_engine(f'postgresql+psycopg2://{psql_user}:{psql_password}@localhost:5432/matt',echo=False)
    df.to_sql(name=table, con=engine, if_exists = 'replace', index=False)
   # print(f'finished writing table {table}')


sql_cnx.close()
