import json
x = {
    "name": "Serdar",
    "age": 30,
    "medeni durum": False,
    "bosanma": True,
    "cocuk": ("Elif","Musa"),
    "evcil hayvan": None,
    "araba": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
    ]  
}

json.dumps(x, indent=4)
print(x)
json.dumps(x, indent=4, separators=(". ", " = "))
print("\n********************",x)
json.dumps(x, indent=4, sort_keys=True)
print("\n********************",x)
#Bu parametre, JSON çıktısında anahtarların alfabetik olarak sıralanmasını sağlar.