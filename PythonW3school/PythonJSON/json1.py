import json

x =  '{ "name":"John", "age":30, "city":"New York"}' #JSON

#parse et
peri = json.loads(x)

print(peri["city"])