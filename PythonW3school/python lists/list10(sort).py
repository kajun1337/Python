#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

my_List = ["fainted", "km" , "cra"]
my_List.sort()
print(my_List)

sayilarim= [32,11,59,44]
sayilarim.sort()
print(sayilarim)

#Sort descending olayı azalan sıralama ypamak? 
#
""" reverse = True parametresi, listeyi azalan (büyükten küçüğe) 
sıralamak için kullanılır. Bu parametre olmadığında, 
sort metodu varsayılan olarak listeyi artan (küçükten büyüğe) sıralar. """

testAnlamak = ["orange", "mango", "kiwi", "pineapple", "banana"]
testAnlamak.sort(reverse=True)
print(testAnlamak)

testSayilar = [98,42,56,11,87]
testSayilar.sort(reverse=True)
print("*" , testSayilar)
