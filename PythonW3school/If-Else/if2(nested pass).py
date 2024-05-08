x = 41
if x > 10:
    print ("41 10 dan buyuk")
    if x > 20:
        print("2.nested if e giris")
    else: 
        print("2.ye dahil olmadan cıkıs")


""" The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error. """

a = 33
b = 200

if b > a:
  pass
  print("pass OK!")
else:
    print("NOT OK")