#The while Loop
i = 1
while i < 6:
  print(i)
  i += 1

#The break Statement
k = 1
while k < 6:
  print(k)
  if k == 3:
    break
  k += 1

#The continue Statement
j = 0
while j < 6:
  j += 1 
  if j == 3:
    continue
  print(j)


#The else Statement
a = 1
while a < 6:
  print(a)
  a += 1
else:
  print("a is no longer less than 6")