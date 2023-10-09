"""
import requests
import json

"""
DATABASE = "starwarsdriven"
USER = 'postgres'
PASSWORD = 'maytheforcebewithyou' #flytta till env variabel
PORT = '5432'
"""

response = requests.get('https://swapi.dev/api/people')

if response.status_code == 200:
    people = response.json()
    people_results = people["results"] #results hold people in API

    
    
    #Du går bara igenom en page nu!
    for person in people_results:
        name = person["name"]
        height = int(person["height"])
        hair_color = person["hair_color"]
        skin_color = person["skin_color"]
        eye_color = person["eye_color"]
        birth_year = person["birth_year"]
        gender = person["gender"]
    




      
    
  
    print("connection closed")


    

else:
    print(f"Error status{response.status_code}")
"""

print('hello!!!!!!!!!!')