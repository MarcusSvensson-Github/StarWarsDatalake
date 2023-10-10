
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

        for film in films: #du vill nu 1.ta ut en film i taget 2.skicka in en lista med deras URLer 
           
            embedded_data = embedded_url_data_fetcher(film['planets'])
            #print(film['planets'], '\n')
            #3. ersätta varje films URLer innehål med nytt innehåll
            film['planets'] = embedded_data

            print(film['planets'])

            print(type(film), '\n\n')



 
        """
        next_page_url = data['next']
        while next_page_url:
            print(next_page_url)
            response = requests.get(next_page_url)
            data = response.json()
            next_page_url = data['next']
            page = data['results']
            result.extend(page)
        """
            
        """
        dataframe = pd.DataFrame(films)  

        engine = create_engine('postgresql+psycopg2://postgres:maytheforcebewithyou@StarWarsDriven/postgres')

        dataframe.to_sql('starwars_films', engine)
        
        """
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
        embedded_data.append(data)
    return embedded_data

 

if __name__ == "__main__":
    build_starwars_db()



