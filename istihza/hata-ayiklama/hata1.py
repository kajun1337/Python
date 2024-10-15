import logging
""" 
    Programcı Hataları (Error)
    Program Kusurları (Bug)
    İstisnalar (Exception) 
"""

logging.basicConfig(level=logging.DEBUG)

veri1 = input("Karekökünü hesaplamak istediğiniz sayı: ")
try:
    
    print(logging.info("Bu bir bilgi mesajıdır."))
    karekök = int(veri1) ** 0.5
    print(veri1, "sayısının karekökü: ", karekök)
except:  # expect ValueError diyebilirdin türe göre farklı expect ler de cıkartabılırsın
    logging.info()
    print("Girdiğin veri sayı mı harbiden?")

veri2 = input("Karesini hesaplamak istediğiniz sayı: ")
kare = int(veri2) ** 2
print(veri2, "sayısının karesi: ", kare)

# Eğer try bloğu içinde belirtilen işlemler sırasında bir ValueError ile karşılaşırsan 
# bunu görmezden gel ve normal şartlar altında kullanıcıya göstereceğin hata mesajını 
# gösterme. Onun yerine kullanıcıya Lütfen sadece sayı girin! uyarısını göster.

""" try:
    hata verebileceğini bildiğimiz kodlar
except HataAdı:
    hata durumunda yapılacak işlem """

