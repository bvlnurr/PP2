#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist2 = ["apple", "banana", "cherry"]
for i in range(len(thislist2)):
  print(thislist2[i])

#Using a While Loop
thislist3 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist3):
  print(thislist3[i])
  i = i + 1

#Looping Using List Comprehension
thislist4 = ["apple", "banana", "cherry"]
[print(x) for x in thislist4]