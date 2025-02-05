import math
mylist = [1,2,3,4,5,65464,7,8,9,]

print(mylist[:7])

for i in mylist:
    print(i)
    mylist[4] += i
    mylist[0] = 56
    
mylist[3] = 7
mylist[3] += 476
print(mylist)

mylist[6].conjugate()

print(mylist)

class list:
    x = 2

list.x = 3

print(list.x)

60 == 5j - 56

comp = 5j - 56

comp.conjugate()

print(comp)

comp2 = 60 == 5j - 56

print(comp2)

print(math.pi)

math.fmo