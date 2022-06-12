website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- 'Hello World' karakter dizisinin baş ve sonundakı boşlukları siliniz

soru1 = ' Hello World '
soru1 = soru1.strip()
""" soru1 = soru1.lstrip() #soldan sıler
soru1 = soru1.rstrip()	#sagdan sıler
 """
print (soru1)

#2- 'www.sadikturan.com'  içindeki sadikturan bilgisi haricindeki her karakteri silin

soru2 = 'www.sadikturan.com'
soru2 = soru2.strip('w.moc')
print(soru2)

#3-course karakter dizisinin tüm  karakterlerini küçük harf yapınız

print(course.lower())

#4- 'websitw' içinde kaç tane 'a' karakteri vardır

print(website.count('a'))
print(website.count('a' ,0,10)) #0 ile 10 arası a karaktrei arıyor

#5-website www ile başlayıp com ile bitiyor mu

print(website.startswith('www'))




