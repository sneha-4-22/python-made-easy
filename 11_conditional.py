a=15
#1 if-elif-else ladder in python 
if(a>3):
    print("the value of a is greater than 3")
elif(a>7):
    print("the value of a is greater than 7")
elif(a>13):
    print("the value of a is greater than 13")
else:                                           #imp <--else is optional-->
    print("the value is not greater than 3 or 7")
print("done")   
#2 multiple if statements
if(a>3):
    print("the value of a is greater than 3")
if(a>7):
    print("the value of a is greater than 7")
if(a>13):
    print("the value of a is greater than 13")
else:
    print("the value is not greater than 3 or 7")
print("done")
#example 1
age=int(input("enter your age:  "))
if(age>=18):
    print("you are an adult")
else:
    print("you are not an adult")
#example 2
age1=34
if(age1>26 and age1<56):
    print("you can work with us , welcome:)) ")
if(age1>26 or age1<56):
    print("you can work with us , welcome:)) ")
else:
    print("sorry!!")