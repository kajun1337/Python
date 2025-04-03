""" % işareti ile biçimlendirme

format() metodu ile biçimlendirme """

# parola = input("parola: ")
# print("Girdiğiniz parola (%s) kurallara uygun bir paroladır!" %parola)
# print("%s ve %s iyi bir ikilidir!" %("Python", "Django"))

""" print("istihza".rjust(15))
print("|%s|" % "istihza".rjust(15))
print("|%s|" % "istihza".ljust(15))
print("format {} metodu".format("zombi")) """
kalkış       = input("Kalkış yeri: ")
varış        = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayısı = input("Bilet sayısı: ")

print("""{} noktasından {} noktasına, 14:30 hareket saatli
sefer için {} adına {} adet bilet ayrılmıştır!""".format(kalkış,
                                                         varış,
                                                         isim_soyisim,
                                                         bilet_sayısı))

                  
metin = "{} noktasından {} noktasına, 14:30 hareket saatli \
sefer için {} adına {} adet bilet ayrılmıştır!"
print(metin.format(kalkış, varış, isim_soyisim, bilet_sayısı))
                                     