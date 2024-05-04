thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
#Duplicates Not Allowed

ikile = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(ikile)
print(len(ikile))

#Contain String, int, boolean, and list data types:

malezya = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(malezya)
print(type(malezya))


#The dict() Constructor (dick -> construct)

#list to dick test 
tuples1 = dict(name = "John", age = 36, country = "Norway")
print(dict(tuples1))






