mydic={
    "pankha":"fan",
    "dadda":"box",
    "vastuu":"item"
}
print("options are",mydic.keys())
a= input("enter the hindi word\n" )
print("the meaning of your word is: ",mydic.get(a))#this syntax won't throw an error if the key is not present
#example 1)
num1=int(input("enter the number 1\n"))     
num2=int(input("enter the number 2\n"))
num3=int(input("enter the number 3\n"))
num4=int(input("enter the number 4\n"))
num5=int(input("enter the number 5\n"))
num6=int(input("enter the number 6\n"))
s={num1,num2,num3,num4,num5,num6}
print(s)
#example 2)
b={18,"18",18.1}#consider as unique value
print(b)
#find out the length of the following set
m=set()
m.add(20)
m.add(20.0)
m.add("20")
print(len(m))#comes out to be 2 not 3 "*_*" as here 20.0=20 but 20.1!=20
#create an empty dic allow four friends to enter their fav language as values and use keys as their name. assume that names are unique
favlang={}
a=input("enter your fav language shivani\n")
b=input("enter your fav language mohan\n")
c=input("enter your fav language dimple\n")
d=input("enter your fav language nidhi\n")
favlang['shivani']=a
favlang['mohan']=b
favlang['dimple']=c
favlang['nidhi']=d
print(favlang)

