class Person:
    pass

class Big_Boy:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def yazdrici(self):
        print(self.firstname, self.lastname)
    # def __str__(self) -> str:
    #     return f"{self.firstname} {self.lastname}"

x = Big_Boy("John","Doe")
# print(x)
x.yazdrici()


""" class Evlat(Big_Boy):
    pass

y = Evlat("Evladi","Johni")
y.yazdrici() """

#When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Evlat(Big_Boy):
    def __init__(self, fname, lname):
      Big_Boy.__init__(self,fname,lname) #Üstten gelen mirası kormak için 
    #dikkat et burada tanımlı degıl fakat child class da kullanım yapabildik

#Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

post = Evlat("Surname" ,"Korname")
post.yazdrici()











