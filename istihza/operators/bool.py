#her sey 1 & 0 dan olusur 1 = True 0 = False    
a = 1
print(a == 1)
print(a == 2)
# 0 değeri ve boş veri tipleri False’tur. Bunlar dışında kalan her şey ise True’dur.
print(bool(3))
print(bool(""))
#bool işleçleri herhangi bir ifadenin doğruluğunu veya yanlışlığını sorgulamak için kullanılabiliyor.

isim = input("Adınızı giriniz: ")
print("Ferhat" == isim)

kullanıcı = input("Kullanıcı adınızı giriniz: ")
if bool(kullanıcı) == True:
    print("Kullanıcı adı doğru")
else:
    print("Kullanıcı adı boş")

#Yukarıdaki ile aynısı aslında aşağıdaki kodda if kullanıcı gizli, true barındıyıor
"""  kullanıcı = input("Kullanıcı adınız: ")

if kullanıcı:
    print("Teşekkürler!") """
