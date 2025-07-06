"""
Write a program to open a file in
different modes (read, write, append),
write data into it,
and read from the file.
"""


# write mode
with open('myfile.txt', 'w') as file:
    file.write("My name is kritika\n")


# append mode
with open('myfile.txt', 'a') as file:
    file.write("My friend name is rekha.\n")

# read mode
with open('myfile.txt', 'r') as file:
    read = file.read()
    print(read)
