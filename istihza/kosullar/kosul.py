import time
import ctypes

print("""Programa hoşgeldiniz!

Programımızı kullanabilmek için en az
13 yaşında olmalısınız.""")

print("Lütfen yaşınızı girin.\n")

yaş = input("Yaşınız: \t")

if int(yaş) != 0 or int(yas) == 1:
    print("ozel durum")
    ctypes.windll.user32.MessageBoxW(0, "Özel durum", "Uyarı", 1)

if int(yaş) <= 13:
    ctypes.windll.user32.MessageBoxW(0, "Üzgünüz, programı kullanmak için 13 yaşından büyük olmalısınız.", "Uyarı", 1)
    time.sleep(3)
    exit("Üzgünüz, programı kullanmak için 13 yaşından büyük olmalısınız.")


yaş = int(input("Yaşınız: "))

if yaş == 18:
    print("18 iyidir!")

if yaş < 0:
    print("Yok canım, daha neler!...")

if yaş < 18:
    print("Genç bir kardeşimizsin!")

if yaş > 18:
    print("Eh, artık yaş yavaş yavaş kemale eriyor!")
    




