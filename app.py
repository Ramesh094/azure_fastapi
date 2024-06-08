import json

customers = {
    "name": 'Ramesh', 
    "age": 20
}

json_obj = json.dumps(customers)
print(type(json_obj))
print(json_obj)

python_obj = json.loads(json_obj)
print(type(python_obj))
print(python_obj)