#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


#Add Sets
thisset1 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset1.update(tropical)

print(thisset1)


#Add Any Iterable
thisset2 = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset2.update(mylist)

print(thisset2)