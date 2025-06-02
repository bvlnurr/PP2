thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])

#Range of Indexes
thistuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple1[2:5])
print(thistuple1[:4])
print(thistuple1[2:])
print(thistuple1[-4:-1])

#Check if Item Exists
thistuple2 = ("apple", "banana", "cherry")
if "apple" in thistuple2:
  print("Yes, 'apple' is in the fruits tuple")