#numeric types: int, float, complex
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#type conversion
#You cannot convert complex numbers into another number type.
x = 3
y = 6.9
z = 6j

a = float(x)
b = complex(y)
c = int(x)

print(a)
print(b)
print(c)


#ramdom number
import random
print(random.randrange(1, 10))