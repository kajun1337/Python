""" count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found """


my_tuple = (1, 2, 3, 1, 4, 1, 5)
count_ones = my_tuple.count(1)
print("1 değeri", count_ones, "kez geçiyor.")
count_toplam = my_tuple.count(2)
print(count_toplam)


meyve = ("soda","elma","armut")
print(meyve.index("armut"))
