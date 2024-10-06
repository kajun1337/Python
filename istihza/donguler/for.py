#for döngüsü while döngüsüne göre biraz daha yeteneklidir

"""
Evet, while ile yapabildiğiniz bir işlemi for ile de yapabilirsiniz çoğu zaman,
ama bu döngülerin, belli vakalar için tek seçenek olduğu durumlar da vardır. 
Zira bu iki döngünün çalışma mantığı birbirinden farklıdır.
"""
tr_harfler = "şçöğüİı"

for harf in tr_harfler:
    print(harf)

# for değişken_adı in değişken:
#     yapılacak_işlem

""" for döngüsü, üzerinde döngü kurulabilecek veri tiplerinin her bir öğesinin üzerinden 
tek tek geçer ve bu öğelerin her biri üzerinde bir işlem yapar. while döngüsü ise herhangi
 bir ifadenin bool değerini kontrol
eder ve bu değerin bool değeri False olana kadar, belirlenen işlemi yapmayı sürdürür. """


 #int (tam sayı) türündeki nesneler üzerinde döngü kuramıyoruz

""" 
sayılar = 123456789

for sayı in sayılar:

    print(sayı) #hata alırız """

""" 
a = "istihza.com"
print("h" in a)

for degisken in a:
    print()


for s in "Python":
    print(s)
 """

tr_karakter = "şçöğüİı"
sifre = input("Bir karakter giriniz: ")
for i in tr_karakter:
    if i in sifre:
        print("TR KARARKTER OLMAZ")
        break
    elif not sifre:
        print("Boş bırakmayınız")
        break







