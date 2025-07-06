"""
https://youtu.be/7QCHpAtlSMo
Bro Code (python keyword argument)
+
telusko(cont..)
"""

#follow pdf slide no 12
# write theory 1st

# keyword argument => an argument preceded by an identifier
#                     helps with readability and
#                     order of argument doesn't matter.
#


#1) positional argument
def greet(greeting,title,f_name,l_name):
    print(f"{greeting}! {title}.{f_name} {l_name}")

greet('Hello',"Mr","Dipesh","Dhaurali")


#2) Keyword argument
def greet(greeting,title,f_name,l_name):
    print(f"{greeting}! {title}.{f_name} {l_name}")

greet(title="Mr",l_name="Dhaurali",greeting='Hello',f_name='dipesh')


#2) other example of keyword argument
def person(name,age):
    print(name)
    print(age)

person(name='Dipesh',age=21)
