"""
cont...(23:50)
"""
# a+ mode is for read and append together ( it add the  string form the end of the file )

file=open('0_demo2.txt','a+')


file.write('I am dipesh')
file.write('I am good boy')
text=file.read()
print(text)
file.close()


"""
notes
-----
0) No result of reading the file ( before and after writing a file)
 
1) a+ mode is a combination of append (a) and read (r).
    -It opens the file for both reading and appending.
    -Any new content is added to the end of the file, without changing the existing content.
    -If the file doesn’t exist, it creates a new one.

2) After writing, the file pointer stays at the end of the file.
    -So if you try to read() right after writing, you’ll get an empty string because there’s nothing to read after the end.
    -To read the file content, you must move the file pointer to the beginning using file.seek(0) before reading.

3) it will add text value at last
"""