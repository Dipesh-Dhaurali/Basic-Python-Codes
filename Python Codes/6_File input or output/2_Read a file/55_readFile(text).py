"""
cont...(12:25)
"""

# Write a program to read a file in a text mode.

file=open("1_demo.txt", "rt")  #r for read and t for text file
text=file.read()
print(text)


file.close()



"""
note
----
1) 'rt' is not composable it is by default 't' at end
2) we can say that all modes are open default in text files 
"""