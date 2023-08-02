import json

with open('info.json', 'r') as f:
    res = json.load(f)

for i in res:
    print(i)
