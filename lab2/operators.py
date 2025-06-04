# Arithmetic operators
x = 2
y = 6

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y) 


# Assignment operators
a = 5, b = 7, c = 2
a += 3
b -= 4
c *= 5  #and so on


print(a)
print(b)
print(c)


# Comparison operators
f = 8, p = 10

print(f == p)
print(f != p)
print(f > p)
print(f < p)
print(f >= p)
print(f <= p)



# Logical operators
k = 15

print(k > 6 and k < 10)
print(k > 11 or k < 8)
print(not(k > 20))


# Identity operators
r = ["apple", "banana"]
u = ["apple", "banana"]

print(r is u)
print(r == u)
print(r is not u)



# Membership operators
n = ["apple", "banana"]

print("banana" in n)
print("apple" not in n)



# Bitwise operators
m = 4, j = 6

print(m & j)
print(m | j)
print(m ^ j)
print(~m)
print(m << 2)
print(m >> 2)