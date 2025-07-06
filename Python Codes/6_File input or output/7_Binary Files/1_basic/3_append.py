# WAP to append a binary file
file=open('data.bin', 'ab')
file.write(b'\y00\y01')

file.close()
#(it is not readable by human because it is made up 0 and 1)
