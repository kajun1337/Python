list=["bmw","mercedes","opel","mazda"]
"""
sonuc = len(list) #listenin boyu bulundu.

sonuc=list[0]
sonuc=list[3]

list[3]="toyota" 

sonuc= "mercedes" in list # Belirtilen verinin listenin elemanı olup olmadığını buluyoruz, çıkış true false olarak gözükecek.

sonuc = list[-2]

sonuc = list[:3]

list[2:4]= ["toyota","renault"]

sonuc= list+["nissan","audi"]

del list[-1] # listenin son elemanını sildik.

sonuc=list[::-1] # listenin elemanlarını tersten yazdırdık.
print(sonuc)  

"""
studentA= ["yigit", "bilgi",2010,[70,60,70]]
studentB= ["sena" ,"turan",1999,[80,80,70]]
studentC= ["ahmet" ,"turan",1998,[80,70,90]]

list1=f"{studentA[0]} {studentB[1]} {2020-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}"


print(list1)

