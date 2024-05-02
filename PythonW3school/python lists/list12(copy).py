""" You cannot copy a list simply by typing list2 = list1, because: 
list2 will only be a reference to list1, and changes 
made in list1 will automatically also be made in list2. """

ozmo =  ["apple", "banana", "cherry"]
testlist = ozmo.copy()
print(testlist)

#Another way to make a copy is to use the built-in method list().

ecnebi = ["apple", "banana", "cherry"]
intel = list(ecnebi)
print(intel)