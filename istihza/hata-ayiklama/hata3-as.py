ilk_sayı    = input("ilk sayı: ")
ikinci_sayı = input("ikinci sayı: ")

try:
    sayı1 = int(ilk_sayı)
    sayı2 = int(ikinci_sayı)
    print(sayı1, "/", sayı2, "=", sayı1 / sayı2)
except ValueError as hata: #Bu şekilde orjinela hata mesajını da bastırabiliyorsun. 
    print("Sadece sayı girin!")
    print("orijinal hata mesajı",hata)

""" Diyelim ki kullanıcıya olası bir hata durumunda hem kendi yazdığınız hata mesajını, 
hem de özgün hata mesajını göstermek istiyorsunuz. İşte yukarıdaki yapı böyle durumlarda işe 
yarayabilir """

