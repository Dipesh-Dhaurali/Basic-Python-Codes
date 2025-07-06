"""
cont...(14:14) (shradha)
"""


# Write a program to read a file with parameter.

file=open("1_demo.txt", "r")

text=file.read(5)  # it only reads the 5 characters
print(text)         # output : I am

file.close()

