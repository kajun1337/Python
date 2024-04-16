message = 'Hello There. My name is Sadık Turan'

""" message = message.upper()  """ #harfleri buyutmek ıcın kullandık 
""" message = message.lower() """ #harfleri kucultmek ıcın kullandık
""" message = message.title() """  # her kelımenın bas harfı buyuk harf olur 
""" message = message.capitalize() """  #verilen strıngın sadece ılk harfını buyuk harfa cevırmıs oluruz
""" message = message.strip() """ #baş ve sonundakı karakterleri silebiliriz bosluk sıldı burada
""" message = message.split()  """ #her bir tanesi ayrı ayrı olarak erişmeye yarıyor cumleyı paracalara ayırıyor
""" message = message.split('.') """ #noktalardan ayıracak cumleyı
""" message = '*'.join(message) """  #öncesinde ayırmazsan her harfin arasına ıstedıgın seyı atar ayrırısan kelımeler arasına da aatabılır
""" message = message.find("Sadık")  """ #cumle ıcersınde kelımeyı aramak 

""" isFound = message.startswith('H') """ #cumle H ile mı baslıyor dıye soruyorum True False donuyor
""" sFound = message.startswith('n')  """#n ile öı bıtıryor

""" message = message.replace('Sadık' , 'Sait' ) """
""" message = message.center(100) """ #conteynır olusturur ortada yazar sag ve sola esıt sekılde web uyguamada açıklama bılgısı ıcın gereklıdır

""" https://www.w3schools.com/python/python_ref_string.asp """

""" print(isFound) """
print(message)
print()
""" print(message[2]) """ #splitle ayırdıktan sonra dırek kelımeyı cekebılıyorsun
