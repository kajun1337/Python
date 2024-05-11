class Person:
    pass

class Big_Boy:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def yazdrici(self):
        print(self.firstname, self.lastname)



class Big_Boy_child(Big_Boy):
    def __init__(self, fname, lname,yas):
      super().__init__(fname,lname)
    #   Big_Boy.__init__(self,fname,lname) alternatif super 'e
      self.yas = yas

    def __str__(self):
        return (self.firstname + self.lastname + str(self.yas))
    
    def tebrik(self):
        print("THY havayolu ile ucan" , self.firstname, self.lastname "yasi " self.yas "olan yolcu")
    
print(Big_Boy_child("Sami","Yusuf",17))


    
    
