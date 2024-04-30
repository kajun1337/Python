meyveler = ["apple", "banana", "cherry", "kiwi", "mango"]
yeni_liste = []

for x in meyveler:
  if "a" in x:
    yeni_liste.append(x)

print(yeni_liste)

#üstekkinin kısa yolu list comprehension ile oluyor alttaki örnekteki gibi

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# newlist = [expression for item in iterable if condition == True]

newlist2 = [x for x in fruits if x != "apple"]
print(newlist2)

newlist3 = [x for x in range(10)]
print(newlist3)
newlist4 = [x for x in range(10) if x < 5]
print(newlist4)
newlist5 = [x.upper() for x in fruits]
print(newlist5)
newlist6 = ['hello' for x in fruits]
print(newlist6)
newlist7 = [x if x != "banana" else "orange" for x in fruits]
print(newlist7)
