""" The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates. """

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.

oA = {"a", "b", "c"}
oB = {1, 2, 3}
oC = oA | oB
print(oC)

#union rastgele birleştiriyor

setx1 = {"a", "b", "c"}
setx2 = {1, 2, 3}
setx3 = {"John", "Elena"}
setx4 = {"apple", "bananas", "cherry"}
setx5= setx1.union(setx1,setx2,setx3,setx4)
setx6 = setx1 | setx2 | setx3 |setx4
print(setx5, end='\n' + str(setx6))

#tuples,sets birlestirme

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
