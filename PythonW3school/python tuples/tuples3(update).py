x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Convert into a list
print("*******************")
thistuple = ("apple", "banana", "cherry")
yas = list(thistuple)
yas.append("orange")
thistuple = tuple(y)

#Add tuple to a tuple

osmanli = ("apple", "banana", "cherry")
bes = ("orange",) # , koydugun için tuples oldu yoksa tuples olmuyor 
osmanli += bes
print(osmanli)

""" Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it,
but you can use the same workaround as we used for changing and adding tuple items: """

rize = ("apple", "banana", "cherry")
okul = list(rize)
print("*-*-", okul)
okul.remove("apple")
rize = tuple(okul)
print(rize)

#Or you can delete the tuple completely:

amasya = ("apple", "banana", "cherry")
del amasya
print("ama",amasya)
