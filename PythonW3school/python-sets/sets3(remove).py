#If the item to remove does not exist, remove() will raise an error.
ecnebi = {"apple", "banana", "cherry"}
ecnebi.remove("banana")
print(ecnebi)

#Remove "banana" by using the discard() method:
# If the item to remove does not exist, discard() will NOT raise an error.
osman =  {"apple", "banana", "cherry"}
osman.discard("banana")
print(osman)

""" You can also use the pop() method to remove an item, but this method will remove a random item, 
so you cannot be sure what item that gets removed.
 """
ismail = {"apple", "banana", "cherry"}
badly = ismail.pop()
print("**",badly)
print("**",ismail)

print("*-*-*-*-*-*-*-*-*-*-")

norm = {"apple", "banana", "cherry"}

norm.clear()

print(norm)

#The del keyword will delete the set completely:

ozmo = {"apple", "banana", "cherry"}

del ozmo

print(ozmo) #hata verir çünkü silinmiş 