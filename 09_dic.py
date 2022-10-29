mydic={
    "penitent":"regretful",
    "amorous" : "showing love",
    "marks":[1,2,3],
    "anotherdict":{'harry':'coder'},
    1:2
}
mydic['marks']=[45,78]
print(mydic['marks'])
print(mydic['anotherdict'])
print(mydic['anotherdict']['harry'])
#dict methods
print(list(mydic.keys()))#prints the keys of the dictionary
print(mydic.values())#prints the values of the dictionary
print(mydic.items())#prints the(key,value)for all contents of the dictionary
print(mydic)
updatedic={
    "lovish":"friends",
    "penitent"  : "remorseful"
}
mydic.update(updatedic)#update the dictionary by adding key value pairs from updatedic
print(mydic)
#diff b/w .get() and [] syntax in dictionary
print(mydic.get("fast1"))#this won't throws an error even if fast1 is not present
print(mydic["fast1"])#throws an error as fast 1 is not present