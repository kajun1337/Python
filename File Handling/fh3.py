f = open("File Handling/test/demofile.b", "r")
print(f.read()) #f.read dosyanın içeriğini okuyup bir string olarak döndürür.



""" Dosyayı açtıktan sonra f değişkeni dosyanın bir işaretçisini içerir. f.read() komutu dosyanın içeriğini okuyup bir
string olarak döndürür. Dolayısıyla, dosya içeriğini görüntülemek için print(f.read()) komutunu kullanırsınız.
Ancak, print(f) komutu, dosyanın işaretçisini (file object) doğrudan yazdırır ve bu, dosyanın içeriğini yazdırmaz, 
sadece dosya nesnesinin durumunu ve konumunu gösterir. Bu nedenle, dosya içeriğini görmek için f.read() veya başka bir
okuma fonksiyonunu kullanmanız gerekir. """



# f = open("D:\\myfiles\welcome.txt", "r") farklı klasörde olduğu zaman bu şekilde bir ayarlanaya yapılması lazım 
 


