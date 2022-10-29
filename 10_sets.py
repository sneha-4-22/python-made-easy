a={1,3,4,5,6,6,8,7,6,8,2}
print(type(a))
print(a)#it will not consider repeating while printing 
b={}#this syntax is consider as dictionary rather than set 
print(type(b))
#an empty set syntax
c=set()
print(type(c))
#set methods
#adding values to set 
c.add(4)
c.add(5)
c.add(3)
c.add([3,6,6,7,7,3])#you can't add list to set but<---- can add tuple to list---->
c.add((4,5,6,7))
c.add({4:5})#can't add dict to sets
print(c)
print(len(a))
a.remove(6)
print(len(a))
print(a.pop())
print(a)

