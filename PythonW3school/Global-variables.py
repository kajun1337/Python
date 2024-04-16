x = "hakan"
y= "killa hakan"

def myfunc():
    print("Git krali" + x)

myfunc()


def lostFunc():
  global x
  x = "fantastic"

lostFunc()


print("Python is " + x)
