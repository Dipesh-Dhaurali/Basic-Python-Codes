"""
cont...(14:14) (shradha)
"""


# Write a program to read a file with line by line.

file=open("1_demo.txt", "r")

text1=file.readline()  # It only read 1st line and skip practise sets
print(text1)         # output :  I am learning Python form apana college (\n)

text2=file.readline() # it only read 2nd line and skip practise sets
print(text2)        #output : I am not feeling well (\n)

file.close()

"""
note:
-----
1) It gates the \n at end by default 
2) It only read 1st line always
"""