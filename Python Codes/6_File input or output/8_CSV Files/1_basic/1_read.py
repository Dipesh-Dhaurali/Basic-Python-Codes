"""
https://youtu.be/hZu-Uwa7WtU?list=PLVJiPhsW8Gnf5rQCOXoptugEtJneB0ZOd

Aditya Aurange (CSV File Handling in Python - Read, Write, Append in CSV File, CSV Module)
Note-: Write Notes form this video
"""


import csv
file=open(r'G:\My Drive\Coding\BOARD_EXAMS\6_File input or output\8_CSV Files\hidden\a.csv','r')
text=csv.reader(file,delimiter=',')
list1=list(text)
print(list1)
file.close()