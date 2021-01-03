import json

with open('data.txt') as json_file:
    data = json.load(json_file)
    data['feeds'].append(("hi",23))
    print(json.dumps(data, indent=2))