fruits = {"orange","apple","banana"}
"""
print(fruits[0]) #sets indekslenemez bir liste olduğundan hata alırız.
"""

for x in fruits: # sets dizisinin elemanlarına ulaşmak için for kullandık.
    print(x)


fruits.add("cherry") # diziye yeni eleman ekledik. bu metodla tek eleman eklenebilir.

fruits.update(["mango","grape"]) # diziye toplu eleman ekledik ama sıraları karışık eklendi.

fruits.remove("mango") #diziden seçilen elemanı çıkartırız.

fruits.discard("apple") #diziden seçilen elemanı çıkartırız.

fruits.clear()#tüm elemanlar silinir.
#sets dizisinde bir eleman sadece bir kez eklenebilir.

mylist=[1,2,3,2,1]
x=set(mylist)#bu metodla listemiz, set listesi haline çevirilir.

print(fruits)

