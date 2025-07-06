"""
follow pdf no(5)
+
book pg (145)
"""
# WAP to write a binary file
file=open('data.bin', 'wb')
file.write(b'x00\x01')

file.close()
#(it is not readable by human because it is made up 0 and 1)
