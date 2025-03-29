import json

json_str='''[{"name":"Alice","age":18},{"name":"Bob","age":38},{"name":"Charlie","age":93},{"name":"David","age":72},{"name":"Emma","age":44},{"name":"Frank","age":96},{"name":"Grace","age":40},{"name":"Henry","age":80},{"name":"Ivy","age":64},{"name":"Jack","age":14},{"name":"Karen","age":77},{"name":"Liam","age":4},{"name":"Mary","age":31},{"name":"Nora","age":25},{"name":"Oscar","age":39},{"name":"Paul","age":39}]'''
data=json.loads(json_str)
sorted_data=sorted(data, key=lambda x: (x['age'], x['name']))
with open("output.json","w") as file:
    json.dump(sorted_data,file,indent=2)