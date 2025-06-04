#Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items
#1. Convert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#2. Add tuple to a tuple
thistuple1 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple1 += y

print(thistuple1)