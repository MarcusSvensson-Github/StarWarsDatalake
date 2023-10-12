
import requests
import pandas as pd
import os
import psycopg2
import time
import json



def extract_starwars_data():
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
            #embedded_data = embedded_url_data_fetcher(film['species'])
            #film['species'] = embedded_data
        
        print('creating folder')
        FOLDER = "object_data/"
        listOfFiles = os.listdir(FOLDER)
        numberOfFiles = len(listOfFiles)
        newFileNumber = numberOfFiles + 1
        filename = f"{FOLDER}/data_v{newFileNumber}.json"
        print(filename)
        print('writing to file')

        with open(filename, "x") as file:
            file.write(films)
        
        
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
        print(link)
        response = requests.get(link)
        data = response.json()
        embedded_data.append(data)
        print('data appended')
    return embedded_data

 
if __name__ == "__main__":
    extract_starwars_data()



