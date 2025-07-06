
#read and write a file with withKeyword
with open('0_demo.txt','r+') as file:
    text=file.read()
    print(text)

    file.write("I am hero")
    text1=file.read()
    print(text)

"""
output (it will ignore 'i am hero')
-------
I am dipeshI am dipeshI am dipesh
I am dipeshI am dipeshI am dipesh

"""