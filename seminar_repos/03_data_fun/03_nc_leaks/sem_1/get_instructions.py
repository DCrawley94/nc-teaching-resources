import requests

body = requests.get("https://nc-leaks.herokuapp.com/api/top-secret").json()

instr = body["instructions"]

with open("instructions.md", "w", encoding="utf8") as f:
    f.write(instr)
