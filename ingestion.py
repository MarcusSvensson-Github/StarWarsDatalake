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
        print(person["name"])
        name = person["name"]
        
    
    

else:
    print(f"Error status{response.status_code}")