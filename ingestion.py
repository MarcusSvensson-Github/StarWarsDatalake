
import requests
import json
import pandas as pd

DATABASE = "starwarsdriven"
USER = 'postgres'
PASSWORD = 'maytheforcebewithyou' #flytta till env variabel
PORT = '5432'


response = requests.get('https://swapi.dev/api/people')

if response.status_code == 200:
    people = response.json()
    people_results = people["results"] #results hold people in API

    
    data = {
        'name': [],
        'height': [],
        "hair_color": [],
        "skin_color": [],
        "eye_color": [],
        "birth_year": [],
        "gender": []
    }

    #Du går bara igenom en page nu!
    for person in people_results:
        
        data['name'].append(person["name"])
        data['height'].append(int(person["height"]))
        data['hair_color'].append(person["hair_color"])
        data['skin_color'].append(person["skin_color"])
        data['eye_color'].append(person["eye_color"])
        data['birth_year'].append(person["birth_year"])
        data['gender'].append(person["gender"])

    print(data)
    

else:
    print(f"Error status{response.status_code}")


