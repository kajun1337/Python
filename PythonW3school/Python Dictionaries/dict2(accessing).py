#You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
y = thisdict.get("model")
print(y)


#The keys() method will return a list of all the keys in the dictionary.

z = thisdict.keys()
print(z)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys() # soldaki değerler key oluyor

print(x) #before the change

car["color"] = "white"

print(end="\n"+str(x)) #after the change
#how to use values() values keys ler soldaki valueler sağdaki
car["color"] = "red"
car["year"] = 2020
print("\n")
print(car.values())

def test():
    return 0


if "branda" in car: 
    print("yes available")
elif "modela" in car:
    print("modelci")
else:
    print(test())


