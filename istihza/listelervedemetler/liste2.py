kardiz = "İstanbul Büyükşehir Belediyesi"
liste = kardiz.split()

for i in liste:
    print(i)
diller = ["İngilizce", "Fransızca", "Türkçe", "İtalyanca", "İspanyolca"]
print(len(diller))

# list() Fonksiyonu
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
isimler = "ahmet mehmet cem"
print(isimler.split())
isimlerIkı = "elma, armut, çilek"
print(isimlerIkı.split(", "))

print(alfabe.split("i"))  # i ye göre ayırır
harf_listesi = list(alfabe)
print(harf_listesi)

meyveler = ["elma", "armut", "çilek", "kiraz"]
print(meyveler[0])
print(meyveler[::-1])
