import os

print("""
[H]=========KAJUNx========[-][o][x]
|                                 |
|     Programa Hoşgeldiniz!       |
|           Sürüm 1.8             |
|    Devam etmek için herhangi    |
|       bir düğmeye basın.        |
|                                 |
|=================================|
""")


print(len("elma"))
print("Python", "PHP", "C++", "C", "Erlang", sep="") #gizli arguman sep bosluk atıyor normalde aralara
print("bir", "iki", "üç", "dört", "on dört", sep=" " + "mumdur" + " ")#Ancak sep parametresine değer olarak yalnızca karakter dizilerini ve None adlı özel bir sözcüğü verebiliriz
print('a','b', sep=None)

print("\n")
print("\n")
#end parametresi ise bu parametrelerin sonuna neyin geleceğini belirler.
print("Pardus ve Ubuntu birer GNU/Linux dağıtımıdır")

"""
Bu kodu yazıp Enter tuşuna bastığımız anda print() fonksiyonu iki farklı işlem gerçekleştirir:

Öncelikle karakter dizisini ekrana yazdırır.

Ardından bir alt satıra geçip bize >>> işaretini gösterir.
"""
print("Pardus\nUbuntu")

print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")
print("Bugün günlerden Salı", end="\n") #By default there is an x parameter like this
print("Bugün günlerden Salı", end=":")

#sys.stdout, ‘standart çıktı konumu’ anlamına gelir
dosya = open("test.txt", "w")
print("Ben Python, Monty Python!", file=dosya)
dosya.close()
print("\n",os.getcwd())
#print("Tahir olmak da ayıp değil", "Zühre olmak da",sep=" ", end="\n", file=sys.stdout) defaultta aslında bu şekilde
#code print number

f = open("test.txt", "w")
print("Merhaba Dünya!", file=f, flush=True) # flush ile close etmeden anlık olarak yaptık.
"""
karakter dizisinin başına eklediğimiz yıldız işareti, bu karakter dizisini tek tek öğelerine ayırıp, bu öğeleri yine tek tek ve sanki her bir öğe 
ayrı bir parametreymiş gibi o fonksiyona gönderdiği için doğal olarak yıldız işaretini ancak, birden fazla parametre alabilen fonksiyonlara 
uygulayabiliriz.
"""
print(*"Linux", sep=".")
#Çünkü yıldızlı parametreler ancak ve ancak dizi özelliği taşıyan veri tipleriyle birlikte kullanılabilir. 

import sys
print(sys.stdout)
sys.stdout

#sayıları ekrana yazan kod lazım
#print logging code
#<_io.TextIOWrapper name='<stdout>' mode='w' encoding='cp1254'> default değer sys.stdout un 

osman = "Araştırma Geliştirme Müdürü"

mehmet = "Proje Sorumlusu"

osman, mehmet = mehmet, osman






