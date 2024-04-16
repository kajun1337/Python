
#key value sistemi
"""
sehirler= ["kocaeli","istanbul"]
plakalar=[41,34]

print(plakalar[sehirler.index("kocaeli")]) #listelerde bu şekilde bilgiyi getirebiliriz.

plakalar = {"kocaeli":41,"istanbul":34} #dictionary şeklinde liste oluşturduk. Key ve value sistemi kullanıldı.

print(plakalar["kocaeli"])

plakalar["ankara"]=6 #dictionary listesine yeni bir key value değeri ekledik.

plakalar["kocaeli"] ="yeni deger" # bu şekilde dictionary listesindeki veriyi de değiştirebiliriz.

print(plakalar)
"""

users={
    "sadikturan":{
        "age":36,
        "roles":["admin"],  # içeride dizide oluşturabiliriz.
        "email":"x.com",
        "address":"kocaeli",
        "phone":"123246"
    },
    "cinarturan":{
        "age":2,
        "roles":["admin","bot"],  # içeride dizide oluşturabiliriz.
        "email":"y.com",
        "address":"kocaeli",
        "phone":"654312"
    }
}

print(users["sadikturan"]["age"]) # dictionary liste metodunda bu şekilde alt listeler oluşturup onlara da bu şekilde ulaşabiliriz.
print(users["cinarturan"]["roles"][0])# Bu şekilde dictionary'nin içinde oluşturulan diziyede ulaşabiliriz.

