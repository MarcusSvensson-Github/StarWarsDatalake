import requests
import json
import psycopg2

DATABASE = "starwarsdriven"
USER = 'postgres'
PASSWORD = 'maytheforcebewithyou' #flytta till env variabel
PORT = '5432'


response = requests.get('https://swapi.dev/api/people')

if response.status_code == 200:
    people = response.json()
    people_results = people["results"] #results hold people in API


    """
    #printar bara ut
    people_result = json.dumps(people['results'])
    print(people_result)
    """
    
    #connecting db
    connection = psycopg2.connect(database = DATABASE, user = USER, password = PASSWORD, port=PORT) #local host at default
    print("connected...")
    connection.autocommit = False
    cursor = connection.cursor()
    
    
    #Du går bara igenom en page nu!
    for person in people_results:
        name = person["name"]
        height = int(person["height"])
        hair_color = person["hair_color"]
        skin_color = person["skin_color"]
        eye_color = person["eye_color"]
        birth_year = person["birth_year"]
        gender = person["gender"]
    

        SQLquery = f"INSERT INTO starwars_people(name, height, hair_color, skin_color, eye_color, birth_year, gender) VALUES('{name}', {height}, '{hair_color}', '{skin_color}', '{eye_color}', '{birth_year}', '{gender}');"
        print(SQLquery)
        cursor.execute(SQLquery)
        connection.commit()

      
    
    #connection.commit()
    cursor.close()
    connection.close()
    print("connection closed")


    

else:
    print(f"Error status{response.status_code}")