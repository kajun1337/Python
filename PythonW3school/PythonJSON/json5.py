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
print(json.dumps(x))
