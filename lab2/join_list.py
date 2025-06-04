#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#Append list_2 into list_1:
list_1 = ["a", "b" , "c"]
list_2 = [1, 2, 3]

for x in list_2:
  list_1.append(x)

print(list_1)

#Use the extend() method to add list2 at the end of list1:
list = ["a", "b" , "c"]
list0 = [1, 2, 3]

list.extend(list0)
print(list)