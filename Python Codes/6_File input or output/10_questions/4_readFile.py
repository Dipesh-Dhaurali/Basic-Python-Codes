"""
https://youtu.be/l1FsnQxET9U?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg

CWH(#50/100)
"""
#WAP in file read with while and if

file=open('1_myfile.txt', 'r')
while True:
    line=file.readline()
    if not line:
        break
    print(line)
