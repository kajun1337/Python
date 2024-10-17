import locale
locale.setlocale(locale.LC_ALL, 'tr_TR.UTF-8')

# Karakter Dizilerini Alfabe Sırasına Dizmek
print(sorted("kitap", key=locale.strxfrm))  # ['a', 'i', 'k', 'p', 't']

# Nasıl input() fonksiyonu çıktı olarak bir karakter dizisi ve len() fonksiyonu bir sayı veriyorsa,
# sorted() fonksiyonu da bize çıktı olarak, birkaç bölüm sonra inceleyeceğimiz ‘liste’ adlı bir veri tipi verir.


#Karakter Dizileri Üzerinde Değişiklik Yapmak


meyve = "elma"
print("E" + meyve[1:])

site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

# Bunun nedeni, karakter dizilerinin değiştirilemeyen (immutable) bir veri tipi olmasıdır.
# Python’da iki tür veri tipi bulunur: değiştirilemeyen veri tipleri (immutable datatypes) 
# ve değiştirilebilen veri tipleri (mutable datatypes). Bizim şimdiye kadar gördüğümüz 
# veri tipleri (sayılar ve karakter dizileri), değiştirilemeyen veri tipleridir. Henüz 
# değiştirilebilen bir veri tipi görmedik.

demet = {site1, site2, site3, site4}
for i in demet:
    print("https://" + i)

for i in site1, site2, site3, site4:
    print("http://", i[4:], sep="")



test_1 = "armut"
print(id(test_1))
test_1_revize = "A" + test_1[1:]
print(id(test_1_revize))    