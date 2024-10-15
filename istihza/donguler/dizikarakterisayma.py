metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama
dilinin adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini,
The Monty Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying
Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar
gerçek böyle olsa da, Python programlama dilinin pek çok yerde bir yılan
figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır."""



harf = input("Bir harf girin: ")
sayı = ''
for s in metin:
    if harf == s:
         sayı += harf
print(len(sayı))


#KELIME SAYDIRMA 
# kelime = input("Bir kelime girin: ")
# sayı = metin.count(kelime)
# print(sayı)



# KELIME SAYDIRMA (space ile)
kelime_sayisi = 1  # İlk kelimeyi say
for karakter in metin:
    if karakter == ' ':
        kelime_sayisi += 1

print("Toplam kelime sayısı:", kelime_sayisi)




