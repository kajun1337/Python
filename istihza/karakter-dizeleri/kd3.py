site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:
    print("site: ", isim[4:-4])


ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca  kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"

# for ata in ata1,ata2,ata3,ata4,ata5:
#     print(ata[0:-1])

""" atasozleri = [ata1,ata2,ata3,ata4,ata5]

i = 0
while i < len(atasozleri):
    print(atasozleri[i][0:-1])
    i += 1
 """
tostman = "Tost makinesi"

 
print(tostman[::-1]) #tersten yazdırma
print(tostman[::2]) #ikişer atlayarak yazdırma
