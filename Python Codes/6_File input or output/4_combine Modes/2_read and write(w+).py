"""
cont...(23:50)
"""
# w+ mode is for read and write together ( overwrite all values)

file=open('0_demo1.txt','w+')


file.write('I am dipesh')
text=file.read()
print(text)
file.close()


"""
notes
-----
0) No result of reading the file ( before and after writing a file)

1) w+ mode is a combination of write (w) and read (r).
   -It opens the file for both reading and writing.
   -However, it overwrites the entire content of the file if it already exists.
    -If the file doesn't exist, it creates a new one.

2) After writing to the file, the file pointer is at the end of the file.

     -So when you call read() right after write(), it returns nothing (empty string) because there’s nothing to read after the current pointer.
     -To read what you wrote, you need to move the file pointer to the beginning using file.seek(0) before reading.

3) it will totally overwrite file text
"""

