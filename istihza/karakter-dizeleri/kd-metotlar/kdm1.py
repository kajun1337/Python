# replace()
kardiz = "elma"
print(kardiz)
print(kardiz.replace("e", "E"))
ornekIkı = "www.google.com"
print(ornekIkı.replace("google", "vpn"))


""" ekrem = "İstanbul Büyükşehir Belediyesi"
print(ekrem[0], ekrem[9], ekrem[20], sep="")
print(ekrem.split()) """

print("\n")
cennet = input("Kısaltmasını ogrenmek istediğin kurum:")
for i in cennet.split():
    print(i[0], end="", sep=".")
print("\n")



