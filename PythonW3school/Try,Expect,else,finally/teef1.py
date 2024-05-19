# x = 13
try:
    print(x)

except NameError:
    print("name error") #NameError, bir ismin tanımlanmamış olması durumunda oluşan bir hata türüdür

except:
    print("expect meydana geldi")
else:
    print("hata yok")

 #try blogu olmasa program cokecek ve hata verecekti
 #istesen daha fazla expect blogu olsuturabılırısn 
finally: 
    print("try excpect bitis dudugu") # sonda ne olursa olsun calısan bölüm
    

