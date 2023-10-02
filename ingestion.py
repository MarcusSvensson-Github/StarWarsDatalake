import requests
import json

response = requests.get('https://swapi.dev/api/people')

if response.status_code == 200:
    people = response.json()
    people_results = people["results"] #results hold people in API


    """
    #printar bara ut
    people_result = json.dumps(people['results'])
    print(people_result)
    """
    
    for person in people_results:
        name = person["name"]
        height = person["height"]
        hair_color = person["hair_color"]
        skin_color = person["skin_color"]
        eye_color = person["eye_color"]
        birth_year = person["birth_year"]
        gender = person["gender"]

        print(name, height, hair_color, skin_color, eye_color, birth_year, gender)    
    

else:
    print(f"Error status{response.status_code}")