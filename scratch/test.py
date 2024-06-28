import requests
from pprint import pprint
import json
r = requests.get("https://nc-leaks.herokuapp.com/api/people")

data = r.json()

pprint(data['people'])
