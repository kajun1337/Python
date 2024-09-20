""" ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28

fiyat = 0.79
kullanım = input("metrokup gir: ")
hangiDonem= input("donem yaz: ")
ay = eval(hangiDonem)

 """
veri = input("yaz:")
exp = eval(veri)
print(exp)               #EVAL tehlikeli kullanıum örnek burada __import__("os").system("dir") yazarsan
#__import__("os").system("dir") bu senın dosyalarını dizinlerini görüntüler

# exec örneği
code = """
for i in range(5):
    print("Exec örneği:", i)
"""
exec(code)  # exec, verilen kodu çalıştırır. Bu örnekte, 0'dan 4'e kadar olan sayıları yazdırır.

url = input("URL hata veriyor: ")
print("Hata! Google Chrome '{}' sitesini bulamadı".format(url))

print("test {} cephane".format(url))
print("{} ve {} iyi bir ikilidir".format("Python", "Django"))

print("{} {} yaşında bir {}dur".format("Ahmet", "18", "futbolcu"))

metin = "{} ve {} iyi bir ikilidir"

metin.format("Python", "Django")


url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın: ")

#Kullanıcıya gösterilecek hata için bir taslak metin oluşturuyoruz
hata_taslağı = "Hata! Google Chrome {} sitesini bulamadı"

print(hata_taslağı.format(url))
