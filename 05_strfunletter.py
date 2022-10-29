letter='''Dear <|NAME|> 
Greetings! from microsoft company . I am excited to tell you about your selection ;
You are selected
whising!!you great success
Date:  <|DATE|>
'''
name=input("enter your name\t")
date=input("enter today's date\t")
letter=letter.replace("NAME",name)
letter=letter.replace("DATE",date)
print(letter)