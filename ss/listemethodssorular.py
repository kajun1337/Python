names = ["Ali","Yagmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]
"""
names.append("Cenk") # dizinin sonuna parametreyi ekledik.

names.insert(0,"Sena") # dizinin başına elaman ekledik.

names.remove("Deniz") # parametreyi diziden sildik.

index = names.index("Deniz") # parametrenin index numarasını bulduk.

result = "Ali" in names # ilk parametre dizide bulunuyormu. True yada false çıktısı alınır.
ab
names.reverse() # Dizinin elemanlarının yerini ters çevirdik.

names.sort() # Dizinin elemanlarını alfabetik olarak sıraladık.

years.sort() # Dizinin elemanlarını nümerik olarak sıraladık.

str="chevrolet,dacia"
result=str.split(",") #string elemanı diziye çevirdik.Çevririlen elemanların arasına parametredeki değer eklenir.

result=min(years)#dizi içindeki minimum değeri alırız.
result=max(years)#dizi içindeki max değeri alırız.

result = years.count(1998) # dizi içinde parametredi değerinin aramasını yapıp, kaç adet bulunduğunu bulduk.

years.clear()# dizideki tüm elemanları sildik.
"""
x= input("marka gir:") # kullanıcıdan 3 tane input alıp bunları diziye ekledik.
y= input("marka gir:")
z= input("marka gir:")

list1= [x,y,z]


print(list1)