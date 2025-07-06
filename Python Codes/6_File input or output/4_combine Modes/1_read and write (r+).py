"""
cont...(22:05)
"""
# r+ mode is for read and write together (overwrite minimum or needed values)

file=open('0_demo.txt','r+')


file.write('HelloWorld')
text=file.read()
print(text)
file.close()


"""
notes
-----
0) if you do read file at first it work as read and write 

0) Only this mode gives us result using reading file after write a file but only specific part which is not replaced yet

1) r+ mode is a combination of read (r) and write (w).
     -It opens the file for both reading and writing without erasing the entire file.
     -It starts writing from the beginning and overwrites only the required portion of the file, depending on what you're writing.

2) After using write(), the file pointer moves to the end of the written text.
      -If you try to use read() immediately after write(), it will only read what's after the pointer.
      -So, if there's no content after what you wrote, you'll see an empty output.
      -Example:
         -If the file had "Hello world" and you wrote "I am dipesh", it becomes:
         -"I am dipeshld" (overwrites first part and keeps remaining characters like ld).
         -To read the full updated content, use file.seek(0) before reading.

3) r+ does not clear the entire file like w+.
     -It only replaces as much as you write, keeping the rest if your new content is shorter than the original.
"""