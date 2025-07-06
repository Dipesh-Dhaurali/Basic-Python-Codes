"""
self
"""

# Write a program to read a file having different path/directory.

file = open(r"G:\My Drive\Coding\BOARD_EXAMS\6_File input or output\1_Intro\0_dipesh.txt", "r")

text = file.read()
print(text)

file.close()
