"""
cont... (9:38) (shradha)
+
code with harry (#49/100)
"""
# Write a program to read a file .

file=open("1_demo.txt", "r")  # File open (IMP step)
text=file.read()

print(text)        # gives the text file characters
print(type(text))  # <class 'str'>

file.close()      #File Close (IMP step)





#note:
"""
1) Mode 'r' should be compulsory to read a file
2) Mode 'r' refers to the read a file
3) If there file dont exist it throws error. (FileNotFoundError)
4) It Read all text of files 
"""