import re

x = "Tazikli su ve cehennem *atesi 50 yedi"
y = re.findall("[abc]",x)
print(y) 
#[]: Bir karakter kümesini ifade eder. Örneğin, [abc] ifadesi "a", "b" veya "c" karakterlerinden herhangi biriyle eşleşir.
print("\n******************************")
a = re.findall("\d+",x)
print(a)
#\: Özel bir diziyi temsil eder veya özel karakterleri kaçırır. Örneğin, \d bir rakamı, \s bir boşluk karakterini temsil eder.
print("\n******************************")
b = re.findall("c.*m",x)
print(b)
#.: Herhangi bir karakteri (satırbaşı karakteri hariç) eşleştirir.
print("\n******************************")
c = re.findall("^Tazikli",x)
print(c)
print("\n******************************")
#^: Bir dizenin başlangıcını belirtir.
d = re.findall("yedi$" ,x)
print(d)
print("\n******************************")
#$: Bir dizenin sonunu belirtir.
e = re.findall("a*b",x)
print(e)
#*: Önceki karakterin sıfır veya daha fazla tekrarını ifade eder.
print("\n******************************")


ecnebi = "The rain in Spain"
matches = re.findall(r"\bin", ecnebi)
print(matches)




