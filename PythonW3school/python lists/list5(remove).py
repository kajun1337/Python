test_List=["fransa" ,"almanya","norvec"]
test_List.remove("norvec")
print(test_List)

# If there are more than one item with the specified value, the remove() method removes the first occurance:



thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index.

thislist.pop(0)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.

thislist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist2.pop()
print(thislist2)

