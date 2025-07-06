# write a file and read it
with open('demo.txt','w') as file:
    file.write('Hello Dipesh')

with open('demo.txt','r') as file:
    text=file.read()
    print(text)