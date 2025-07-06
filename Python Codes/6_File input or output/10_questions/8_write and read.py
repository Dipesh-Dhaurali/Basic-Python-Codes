# write a file and read it
with open('demo.txt','w+') as file:
    file.write('Hello Dipesh')
    file.seek(0)
    text=file.read()
    print(text)

    print(file.tell()) # tell us the pointer position