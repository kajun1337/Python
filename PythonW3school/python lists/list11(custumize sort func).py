#50 ye olan uzaklık gibi

def fonksiyon(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = fonksiyon)
print(thislist)

#Case Insensitive Sort (buyuk kucuk harf duyarsız)

ecnebi = ["banana", "Orange", "Kiwi", "cherry"]
ecnebi.sort()
print(ecnebi)


#Reverse Order tersine çevirir

tersine = ["banana", "Orange", "Kiwi", "cherry"]
tersine.reverse()
#print(thislist)

#Buyuk harf kucuk har duyarlı

oblok = ["banana", "Orange", "Kiwi", "cherry"]
oblok.sort(key = str.lower)
print(oblok)


