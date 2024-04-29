ahmak = ["apple", "banana", "cherry"]
print("önceki {}", format(ahmak))
ahmak[0] = "test"
print("\n sonraki:{}", format(ahmak))
str = "tatil"
x = f"aaa{str}asdsada"
y = ("ebucehil {}aaaa {}" .format(str,str))
z = (f"kozmopolitik  {str}")
print(x)
print(y , str)
print(z)
print(x + y + z)

ef = f"My name is {str}"
print(ef)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:


thislist2 = ["apple", "banana", "cherry"]
thislist2[1:3] = ["watermelon"]
print(thislist2)

