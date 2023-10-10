
import requests
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import time



def starwars_people_table():
    response = requests.get('https://swapi.dev/api/people')
    if response.status_code == 200:
        data = response.json()

        result = data["results"]    #results hold people in API
        print('result type:', type(result))
        print('fetching:', result[0]['name'])
        next_page_url = data['next']

        while next_page_url:
            print(next_page_url)
            response = requests.get(next_page_url)
            data = response.json()
            next_page_url = data['next']
            page = data['results']
            result.extend(page)

            
        
        dataframe = pd.DataFrame(result)  

        engine = create_engine('postgresql+psycopg2://postgres:maytheforcebewithyou@StarWarsDriven/postgres')

        dataframe.to_sql('starwars_people', engine)
    
    else:
        print(f"Error status{response.status_code}")


if __name__ == "__main__":
    starwars_people_table()



