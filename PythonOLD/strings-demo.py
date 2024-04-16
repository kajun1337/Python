from gettext import find


website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#1- course karakter dizisinde kaç karakter bulunmaktadır
x = len(course)
print(x)
print(len(course))
print("{} kadar karakter var" .format(len(course)))
#2-website içindeki www karakterlerini alın 
print(website[7:10])
print(website.find("www"))

#3-website içinden com karakterlerini alın

print(website[22:25])
websitelen = len(website)
print(website[websitelen-3:websitelen])

#4- course içinden ilk 15 ve son 15 karakterlerini alın

z = course[0:15] # = course[:15] aynı anlamı var
m = course[(x-15):x] # = course[-15:] = course[-15:-1]
print("ilk 15: {} son 15 : {}" .format(z,m))


#5- course ifadesindeki karakterleri tersen yazdırın 

print(course[::-1]) 		#:: -> bunun anlamı butun karakterlerı al -1 1er 1er tersteb git				#print(course[::]) 


name , surname , age ,job = 'Bora' ,'Yılmaz',32,'Muhendis'
#6 Yukarıda veilen  değişkenler ile ekrana aşağıdaki ifadeyi yazdırın 'Benim adım Bora yılmazi Yaşım 32 ve mesleğim mühendis

print("Benim adım" + name+ " " + surname + ", yaşım" + str(age) + "ve meslegim" + job)
print("Benim adım {} , {} Yaşım {} ve mesleğim {}" .format(name,surname,str(age),job))
print(f"Benim adım {name} , {surname} Yaşım {age} ve mesleğim {job}")


#7- 'Hello world' ifadesindeki w ifadesini W ile değiştirin
oppo = "Hello world"
h = oppo[0:6] + 'W' + oppo[-4:] #stringşn icini değistiremedık ama 0 dan 6.indise kadar aldık sonra W ekledik 7.indisi geçip geri kalanı yazdık 
print(oppo)
print(h)
print(oppo.replace('w','Y')) 
#8- 'abc' ifadesini yanyana 3 kere yazdırın 

print("abc" * 3) #3 kere yazdırmıs olduk 
lor = 'abc' * 3 
print(lor)


