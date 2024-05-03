efecan = {"elma" , "armut" , "kelmahmut"}

#Set items are unordered, unchangeable, and do not allow duplicate values
print(efecan)
ahir = {"apple", "banana", "cherry", "apple"}
print(ahir)

""" Note: The values True and 1 are considered the same value in sets, 
and are treated as duplicates: """

cevher = {"apple", "banana", "cherry", True, 1, 2}
print(cevher)

enes = {"apple", "banana", "cherry"}

print(len(enes))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(type(set4))


ehli = set(("apple", "banana", "cherry")) # note the double round-brackets
print(type(ehli))