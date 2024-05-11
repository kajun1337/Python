"""  Python does not have built-in 
support for Arrays, but Python Lists can be used instead. """


cars = ["BMW" ,"Tofas" , "Volvo"]
x = cars[1]
print(x)
cars[0] = "Suzuki"
print(cars[0])
print(len(cars))


cars.append("Honda")
for i in cars:
    print(i)

cars.pop(0)
for i in cars:
    print("*",i)

cars.remove("Volvo")
for i in cars:
    print("-",i)

#The list's remove() method only removes the first occurrence of the specified value.
