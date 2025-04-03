liste = ["öğe1", "öğe2", "öğe3"]
print(type(liste))
listeiKi = ["Ahmet", "Mehmet", 23, 65, 3.2]
for x in listeiKi:
    print(x, end=" *")

listeUc = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"], 34, 65, 33, 5.6]

print(type(listeUc))
for y in listeUc:
    tip = type(y)
    print(f"{tip} için olay bu")
print("\n**************************************************")
print("\n**************************************************")
print("\n**************************************************")

topluDir = dir(str)
sayac = 1
for jey in topluDir:
    if "_" not in jey[0]:
        print(sayac, "-", jey)
        sayac += 1
