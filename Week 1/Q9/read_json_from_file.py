import json
with open('data.json') as f:
    data = json.load(f)
print(data)

with open('output.json','w') as file:
    json.dump(data, file, indent=4)
    
