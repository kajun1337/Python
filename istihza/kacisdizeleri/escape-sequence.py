print('Yarın Ankaraya\'ya gidiyorum.') # "\" bu kacıs dizelerinden birisi
print("\"book\" kelimesi Türkçede \"kitap\" anlamına gelir.") # ters taksim ile devam
print("terubelı \"masor\" ilanıdır") 
print('İstanbul\'un 5 günlük hava durumu tahmini')


print("Python 1990 yılında Guido Van Rossum \
tarafından geliştirilmeye başlanmış, oldukça \
güçlü ve yetenekli bir programlama dilidir.") #uzun karakter dizilerini bölmek için de kullanabiliriz. 

#Satır Başı (\n)
print("birinci satır\nikinci satır\nüçüncü satır")
başlık = "Türkiye'de Özgür Yazılımın Geçmişi"
print(başlık, "\n", "-"*len(başlık), sep="")  #- cizgisi yazının uzunlguuna denk olacak şekilde


#print("C:\nisan\masraflar.txt") #istemsız olarak \n kullanmıs olduk ozel kacıs dizesi yani
#open("C:\nisan\masraflar.txt") 
print("C:\\nisan\masraflar") 
print("C:\\nisan\\masraflar")
print("C:/nisan/masraflar")
#Sekme (\t)

print("abc\tdef") #tab atıyor
print(*"123456789", sep="\t")
#open("C:\\nisan\\masraflar\\toplam_masraf.txt")  #Escape sequence problem, use double backslash or raw string

# Zil Sesi (\a)

print("\a")
print("\a" * 10)
print("C:\\aylar")

# Aynı Satır Başı (\r)
"""
Ancak eğer karakter dizisinin herhangi bir yerine \r adlı kaçış dizisini yerleştirirsek, 
bu kaçış dizisinin bulunduğu konumdan itibaren aynı satırın başına dönülecek ve \r kaçış
dizisinden sonra gelen bütün karakterler satır başındaki karakterlerin üzerine yazacaktır.
"""
print("Merhaba\rDünya")

#Düşey Sekme (\v)

print("düşey\vsekme")

# Küçük Unicode (\u)

# i harfi: \u0130

print("\u0130")
"""
UNICODE, karakterlerin, harflerin, sayıların ve bilgisayar ekranında gördüğümüz öteki
 bütün işaretlerin her biri için tek ve benzersiz bir numaranın tanımlandığı bir sistemdir
"""


# Büyük Unicode (\U)

#Bu kaçış dizisi de, tıpkı \u gibi, UNICODE kod konumlarını temsil etmek için kullanılır. Ancak U ile gösterilen kod konumları u ile gösterilenlere göre biraz daha uzundur. 
print("\U0001F984")


#Uzun Ad (\N)

import unicodedata
print(unicodedata.name('a'))

print(r"Kaçış dizileri: \, \n, \t, \a, \\, r")
