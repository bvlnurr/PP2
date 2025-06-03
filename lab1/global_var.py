#...
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

#...
a = "awesome"
def mufunc():
    print("Python is " + a)

myfunc()

print("Python is " + a)

#keyword "global"
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)