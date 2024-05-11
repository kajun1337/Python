class Sahsi:
 def __init__(self,name,age):
  self.name = name
  self.age = age
    

 def __str__(self) -> str:
  return("hello my name is " + self.name + "and I am {} YO".format(self.age))


"""  def myfunc(self):
   print("Hello my name is " + self.name) """


p1 = Sahsi("John" , 36)
print(p1)


