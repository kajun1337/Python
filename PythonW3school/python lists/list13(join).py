list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Another way to join two lists is by appending all the items from list2 into list1, one by one:

last1= ["a", "b" , "c"]
last2 = [1, 2, 3]

for x in last2:
    last1.append(x)

print(last1)

#Or you can use the extend() method, where the purpose is to add elements from one list to another list:

ehli1 = ["a", "b" , "c"]
ehli2 = [1, 2, 3]

ehli1.extend(ehli2)
print(ehli1)


#ınsert test

memin1 = [10,11,12,54,18,19]
memin1.insert(3,"aa")
ali = memin1.copy()
print(ali)