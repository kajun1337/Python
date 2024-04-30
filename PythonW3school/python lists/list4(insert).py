thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "watermelon")
print(thislist)

#To insert a list item at a specified index

#To add an item to the end of the list, use the append() method:

appendlist = ["apple", "banana", "cherry"]
appendlist.append("cilek")
print(appendlist)



#EXTAND list
turksat = ['turkcell' , 'vodafone' , 'turktelekom']
ecem = ['bimcell' , 'vestelcell']
turksat.extend(ecem)
print(turksat)

""" Add Any Iterable

The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.) """

ibo=["bir" , "iki", "üc"]
sagir= {"name": "John", "age": 30}
cem = ("kiwi","orange")
ibo.extend(sagir.keys())
print(ibo)



