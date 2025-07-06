"""
cont....(14"28)
"""
import csv
file=open(r'G:\My Drive\Coding\BOARD_EXAMS\6_File input or output\8_CSV Files\hidden\b.csv','w')
text=csv.writer(file,delimiter=',')
text.writerow([5,6,7,8,9])

text.writerows([[1,[2,3],4],[6,[7,8],9]])

file.close()