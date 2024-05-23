import os
import time



if os.path.exists("File Handling/test/demofile copy.b"):
    print("dosya mevcut sileyim mi")
    yorn = input("Y/N: ")
    if yorn.lower() == "y":
        os.remove("File Handling/test/demofile.b")
        #os.rmdir("myfolder") dosyada sildirebilin
        print("dosya silindi")
    else:
        print("Programdan cıkıs yapılıyor")
        time.sleep(4)
        exit()

print("işlemler gerçekleşti")


