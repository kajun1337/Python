#lower()
kişi = input("Aradığınız kişinin adı ve soyadı: ")
kişi = kişi.lower()

if kişi == "ahmet öz":
    print("email: aoz@hmail.com")
    print("tel  : 02121231212")
    print("şehir: istanbul")

elif kişi == "mehmet söz":
    print("email: msoz@zmail.com")
    print("tel  : 03121231212")
    print("şehir: ankara")

elif kişi == "mahmut göz":
    print("email: mgoz@jmail.com")
    print("tel  : 02161231212")
    print("şehir: istanbul")

else:
    print("Aradığınız kişi veritabanında yok!")

    iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"

iller = iller.replace("I", "ı").replace("İ", "i").lower()
print(iller)