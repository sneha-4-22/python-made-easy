l1=[1,8,5,5,7,2,4,21]
l1_sorted=l1.sort()
print(l1_sorted)#this will not work
l1.sort()
print(l1)#but this will
l1.reverse()
l1.append(45)#add at the end of the list
l1.insert(0,55)#insert 55 at index 0
l1.pop(2)#removes element at index 2
l1.remove(5)#removes 5 from the list 
print(l1[0]+l1[1]+l1[6])
print(sum(l1))
