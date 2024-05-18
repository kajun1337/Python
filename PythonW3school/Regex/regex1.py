import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x ,"\n******************")

""" - **`^`**: Bir desenin başlangıcını belirtir. Yani, **`^`** karakteri bir desenin metnin başlangıcında olması 
gerektiğini ifade eder. Örneğin, **`^The`** deseni, metnin başında "The" kelimesiyle başlayan bir deseni eşleştirir.
- **`$`**: Bir desenin sonunu belirtir. Yani, **`$`** karakteri bir desenin metnin sonunda olması gerektiğini ifade eder.
Örneğin, **`Spain$`** deseni, metnin sonunda "Spain" kelimesiyle biten bir deseni eşleştirir.

Bu örnekteki **`^The.*Spain$`** deseni, metnin başlangıcında "The" kelimesiyle başlayıp sonunda "Spain" kelimesiyle 
biten bir deseni eşleştirir. **`.*`** ifadesi, herhangi bir karakterin sıfır veya daha fazla tekrarını temsil eder, 
bu nedenle bu desen, "The" ile başlayan ve "Spain" ile biten herhangi bir metni eşleştirir. """

enes = "Mac buyuktur diger vendorlerden"
# y = re.search("^Mac*.vendor.*" ,enes)
y = re.search("^Mac.*vendor.*" ,enes)
print(y)














