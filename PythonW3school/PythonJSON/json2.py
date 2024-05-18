import json

people = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "Los Angeles"},
    {"name": "Dave", "age": 35, "city": "Chicago"},
    {"name": "Anna", "age": 22, "city": "Miami"},
    {"name": "Mike", "age": 28, "city": "San Francisco"},
    {"name": "Laura", "age": 33, "city": "Boston"},
    {"name": "Kevin", "age": 27, "city": "Seattle"},
    {"name": "Sarah", "age": 24, "city": "Denver"},
    {"name": "Chris", "age": 29, "city": "Atlanta"},
    {"name": "Molly", "age": 31, "city": "Dallas"}
]

#parse
""" people_json = json.dumps(people)
veri = json.loads(people_json)
print(veri[0]["name"]) """

# Python objesini JSON stringine çevir
people_json = json.dumps(people)

# JSON stringini Python objesine çevir
veri = json.loads(people_json)

# İlk kişinin adını yazdır
print(veri[2]["name"])
print(veri[0]["city"])
