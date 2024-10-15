try:
    ...bir takım işler...
except birHata:
    ...hata alınınca yapılacak işlemler...
finally:
    ...hata olsa da olmasa da yapılması gerekenl

    finally.. bloğunun en önemli özelliği, programın çalışması sırasında herhangi bir hata gerçekleşse 
    de gerçekleşmese de işletilecek olmasıdır. Eğer yazdığınız programda mutlaka ama mutlaka
    işletilmesi gereken bir kısım varsa, o kısmı finally... bloğu içine yazabilirsiniz.

try:
    dosya = open("dosyaadı", "r")
    ...burada dosyayla bazı işlemler yapıyoruz...
    ...ve ansızın bir hata oluşuyor...
except IOError:
    print("bir hata oluştu!")
finally:
    dosya.close()