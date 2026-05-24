import json

#Dumps

data = {
    "name": "Ala",
    "age": 25,
    "city": "Warszawa"
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))

print (json.dumps(data, indent = 4, ensure_ascii = False ))

#Loads

json_string = '{"name": "Ala", "age": 25, "city": "Krakow"}'
data = json.loads(json_string)

print(data)
print(type(data))


user = {
    "username": "test123",
    "actve": True,
    "score": 42
}

json_data = json.dumps(user, indent = 2)
print(json_data)

back_to_python = json.loads(json_data)
print(back_to_python["username"])

# writting to the file = json.dump"

with open("dane.json", 'w', encoding="utf-8") as f:
    json.dump(user, f, indent = 4, ensure_ascii=False)


# loading from the file: json.load"

with open("dane.json", "r", encoding="utf-8") as f:
    data_file = json.load(f)

print(data_file)
print(type(data_file))