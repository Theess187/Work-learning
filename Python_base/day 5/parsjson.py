import json

with open("log.json") as f:
    data = json.load(f)

print(data["level"], data["message"])
