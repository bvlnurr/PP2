#Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items
thislist2 = ["apple", "banana", "cherry"]
thislist2.insert(1, "orange")
print(thislist2)

#Extend List
thislist3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical)
print(thislist3)

#Add Any Iterable
thislist4 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist4.extend(thistuple)
print(thislist4)