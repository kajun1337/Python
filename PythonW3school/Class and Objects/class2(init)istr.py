class Insan:
    def __init__(self,isim,yas) -> None:
        self.isim = isim
        self.yas = yas
    
insan1 = Insan("John" , 36)

print(insan1.isim)
print(insan1.yas)


""" class Cennet:
    def __str__(self,name,age):
        self.name = name
        self.age = age
p1 = Cennet("John" , 36)
print(p1) """

class Yagsai:
    def __init__(self,ad,yas) -> None:
        self.ad = ad 
        self.yas = yas
    def __str__(self):
        # return f"{self.ad}({self.yas})" 
        return "{}({})".format(self.ad,self.yas)
p1 = Yagsai("john",36)
print(p1)




    

    
