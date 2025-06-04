#Sort List Alphanumerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
thislist1 = [100, 50, 65, 82, 23]
thislist1.sort(reverse = True)
print(thislist1)

#Customize Sort Function
def myfunc(n):
  return abs(n - 50)

thislist2 = [100, 50, 65, 82, 23]
thislist2.sort(key = myfunc)
print(thislist2)

#Case Insensitive Sort
thislist3 = ["banana", "Orange", "Kiwi", "cherry"]
thislist3.sort()
print(thislist3)

#Reverse Order
thislist4 = ["banana", "Orange", "Kiwi", "cherry"]
thislist4.reverse()
print(thislist4)