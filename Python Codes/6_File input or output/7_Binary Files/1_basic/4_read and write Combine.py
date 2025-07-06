# WAP to read and write a binary file
file=open('data.bin', 'rb+') #wb+ #ab+
file.write(b'\c04\c05')

file.seek(0)
binary=file.read()
print(binary)

file.close()

