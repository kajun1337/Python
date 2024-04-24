#Merge variable a with variable b into variable c:
a = "DrFarFar"
b = "Elaxi"
c = a + b
print(c)
f = a + " " + b
print(f)

age = 36
txt = f"My name is John, I am  + {age}"
print(txt)

marka = 911
solo = "kozmo"+ str(marka) + "fiyat nedir?"
print(solo)


yas = 36
zombi = "My name is John, and I am  {}"
print(zombi.format(yas))
print(zombi + str(yas))
print(zombi, str(yas))
print("\n {}******** {}" ,format(yas).format(zombi))

