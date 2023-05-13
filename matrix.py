import json
with open('data.json') as f:
   data = json.load(f)
print(data)

#load -> converts json strings to py(ty:dict)
#dump -> converts py(ty:dict) to json strings
