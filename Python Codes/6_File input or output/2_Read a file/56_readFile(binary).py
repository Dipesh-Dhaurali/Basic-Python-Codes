"""
cont...(12:31)
"""

# Write a program to read a file in a binary mode.

file=open("1_demo.txt", "rb")  #r for read and b for binary file
text=file.read()
print(text)


file.close()



"""
note
----
1) In 'rb' 'b' is complementary to add at end for binary files 
"""