import pandas as pd
from sqlalchemy import create_engine, select
import psycopg2


conn = psycopg2.connect(database='postgres', user='postgres', password='maytheforcebewithyou', port="5432")

with conn:
    with conn.cursor() as curs:
        curs.execute('select * from raw_starwars_planets')
        sql_response = curs.fetchone()
        print(sql_response)

conn.close()