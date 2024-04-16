
ogrenciler={} #ogrenciler dizisine yeni elaman ekleyeceğiz.
x=input("ogrenci no gir:")
y=input("ad gir:")
z=input("soyad gir:")
t=input("tel gir:")

ogrenciler.update({ #yeni eleman eklemek icin update metodunu kullandık.
    x:{
        "ad":y,
        "soyad":z,
        "tel:":t
    }

})
x=input("ogrenci no gir:")
y=input("ad gir:")
z=input("soyad gir:")
t=input("tel gir:")

ogrenciler.update({ #yeni eleman eklemek icin update metodunu kullandık.
    x:{
        "ad":y,
        "soyad":z,
        "tel:":t
    }

})
x=input("ogrenci no gir:")
y=input("ad gir:")
z=input("soyad gir:")
t=input("tel gir:")

ogrenciler.update({ #yeni eleman eklemek icin update metodunu kullandık.
    x:{
        "ad":y,
        "soyad":z,
        "tel:":t
    }

})
print(ogrenciler)
value=input("istenen ogrenci no:") #istenen öğrencilerin verilerini yazdırıyoruz.
print(f"istenen {value} nolu ogrencinin ismi {ogrenciler[value]['ad']} soyismi {ogrenciler[value]['soyad']}'dır")





