ankara = "ankara simidi"
print(ankara[:5].upper(), ankara[5:], sep="")
# SORUGLAYICI METHODLAR

print(ankara.islower())  # Tum harfler kucukse True doner
print(ankara.isupper())  # Tum harfler buyukse True doner

# endswith()

kardiz = "istihza"
print(kardiz.endswith("a"))  # neyle bitiyor


d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"

demet = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11]
for i in demet:
    if i.endswith(".mp3"):
        print(i)
    else:
        pass
# startswith()¶
ecnebi = "python"

print(ecnebi.startswith("p"))
