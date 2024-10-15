hakkında = open("hakkında", encoding="utf-8")#with ile dosyayı daha güvenli açabilirsin.
harf = input("Sorgulamak istediğiniz harf: ")

sayı = 0

for karakter_dizisi in hakkında:
    for karakter in karakter_dizisi:
        print(karakter)
#        if harf == karakter:
#            sayı += 1
#print(sayı)