"""
cont...(18:18)
"""


# Write a program to write a file using append mode.

file = open("0_dipApp.txt", "a")

file.write("My name is dipesh")  #check file it will ADD to the previous text at the end of the file

file.close()


"""
1) It is Add the text to the end of the file
2) It start writing the file form the end of the text of file 
3) If we run multiple times this code it will add text multiple time to file itself
4) If the file is exist then it will app in that file if not it will create a new one and write inside it
"""