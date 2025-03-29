import json
json_str='{"Name":"Anish Sharma","Age":22}'
data=json.loads(json_str)

json_str=json.dumps(data,indent=2)
print(json_str)