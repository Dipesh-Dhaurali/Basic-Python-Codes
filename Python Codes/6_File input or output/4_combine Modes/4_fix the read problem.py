"""
chatgpt (self)
"""
# fix the read problem using combine modes (r+ , w+ , a+)

"""

There is not possible to read and write at same time in (w+ and a+ mode (before and after using write mode))
because the output wont work or print empty string
so we need to use '.seek()' method to move pointer at starting 
and it will fix the reading issue

-Even though the (r+) mode is working but only for not overwritten value otherwise
 it wont work(for after writng a file try to read)
-if we try to read the file in staring before write a file in (r+) it will work
- because its name is r+ which refer to read so it work but not always
"""


file=open('0_demo.txt','a+')   #'w+'   #'r+'    (work for all same code)

file.write('I am dipesh')

file.seek(0)        #it will move pointer to staring
text=file.read()
print(text)
file.close()

