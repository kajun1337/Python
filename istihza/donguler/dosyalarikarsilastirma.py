from pathlib import Path

current_dir = Path(__file__).parent

d1_path = current_dir / "isimler1.txt"
d2_path = current_dir / "isimler2.txt"

d1 = open(d1_path, encoding="utf-8")
d1_satirlar = d1.readlines() # satırları okuyoruz
d2 = open(d2_path, encoding="utf-8")
d2_satırlar = d2.readlines() 

for i in d2_satırlar:
    if not i in d1_satirlar:
        print(i)
d1.close()
d2.close()
