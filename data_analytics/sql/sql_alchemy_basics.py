import psycopg2
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

'''https://suhas.org/sqlalchemy-tutorial/'''


def mySQL_to_pSQL():
    sql_cnx = mysql.connector.connect(user='', password='', port='',
                                  host='',
                                  database='')
    #sql_cur.execute("SHOW STATUS LIKE 'Ssl_cipher'")
    #sql_cur.execute('SELECT * FROM comment')

    table_df = pd.read_sql('SELECT * FROM comment', con=sql_cnx)

    engine = create_engine('postgresql+psycopg2://amelia:test@localhost:5432/matt',echo=False)
    df.to_sql(name='comment', con=engine, if_exists = 'replace', index=False)

    sql_cnx.close()
