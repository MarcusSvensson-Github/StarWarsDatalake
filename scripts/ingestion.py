
import requests
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import time
import json



def build_starwars_db():
    """
    pipeline for starwars api
    """

    response = requests.get('https://swapi.dev/api/films')
    if response.status_code == 200:
        data = response.json()

        films = data["results"]   #contain the api body of interest with films as list
        
        for film in films: #unpack embedded name data from ulr
            embedded_data = embedded_url_data_fetcher(film['planets'])
            film['planets'] = embedded_data
            embedded_data = embedded_url_data_fetcher(film['species'])
            film['species'] = embedded_data

        print(films[0])
            
        dataframe = pd.DataFrame(films)  

        engine = create_engine('postgresql+psycopg2://postgres:maytheforcebewithyou@StarWarsDriven/postgres')

        #skapa tabell data - hash id för få in datan som json

        dataframe.to_sql('starwars_films', engine, if_exists ='replace')
        
        
    else:
        print(f"Error status{response.status_code}")


def embedded_url_data_fetcher(column):
    """ 
    Fetch all data 

    input: str -> json key name with list of api urls
    output: json -> fethed data as list of each url
    """
    embedded_data = []
    for link in column: 
        response = requests.get(link)
        data = response.json()
        embedded_data.append(data['name'])
    return embedded_data

 
if __name__ == "__main__":
    build_starwars_db()



