# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  """ Bu kod, thislist listesindeki her öğeyi (x değişkenine atanır) alır 
  ve onu ekrana basar. Burada, 
  x her iterasyon için listenin bir sonraki öğesine otomatik olarak güncellenir. """

  y = 0
  while(len(thislist) > y):
   print("*" + thislist[y])
   y += 1

   
""" Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

Example
Print all items by referring to their index number: """

heceler = ["apple", "banana", "cherry"]
for i in range(len(heceler)):
  print("TOPsecret",heceler[i])


  top  = ["sado","mazo"]
print(range(len(top)))

