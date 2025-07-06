"""
cont...
"""
#search if the word "learning " exists in the file or not

with open('1_myfile.txt','r') as file:
    text=file.read()


if 'learning' in text:
    print('It exist')
else:
    print("It doent exist")


#other method (not good method)
with open('1_myfile.txt','r') as file:
    text=file.read()

if text.find('learning')!=-1:
    print('Found')
else:
    print('Not found')
