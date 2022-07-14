# özel bir liste tipidir.

list=[1,2,3]

t=(1,"iki",3) # tuple tipi listedir.
"""
print(type(list))
print(type(t))

print(list[2]) # diziyle aynı sonucu alıyoruz tupledada
print(t[2])

print(len(t)) # diziyle aynı sonucu alıyoruz tupledada
print(len(list))

list[0]="ahmet" 
t[0]="deniz" # tuple'da elemanı sonradan değiştiremeyiz hata alırız.

#tuple'da method olarak 2 tane method kullanabiliriz. count ve index
"""

t1=("damla","ayse")
t2=("qwert","trewq")+t1 # tuple da bu şekilde listeye ekleme yapabiliriz.

print(t2)

