import requests
import json

response = requests.get('https://swapi.dev/api/people')

if response.status_code == 200:
    people = response.json()
    print(json.dumps(people))


print()