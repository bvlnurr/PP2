#boolean values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#...
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#bool() function
print(bool("Hello"))
print(bool(15))
print(bool(False))
print(None)
print("")


#functions can return a boolean
def myFunction():
    return True

print(myFunction())

#...
x = 200
print(isinstance(x, int))