
# WAP to read a binary file
file=open('data.bin', 'rb')
binary=file.read()
print(binary)

file.close()
#(it is not readable by human because it is made up 0 and 1)
