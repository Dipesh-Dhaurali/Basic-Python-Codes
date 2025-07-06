"""
cont...(17:53)
"""


# Write a program to write a file using w mode.

file = open("0_dipWrite.txt", "w")

text = file.write("It will overwrite the file")  #check file it will overwrite to the previous text
print(text)   #26  ( it will print the nuber of character)

file.close()


"""
1) It is overwrite the previous file
2) It start writing the file form the beginning 
3) If we run multiple times this code it will overwrite itself
4) If the file is exist then it will write in that file if not it will create a new one and write inside it
"""