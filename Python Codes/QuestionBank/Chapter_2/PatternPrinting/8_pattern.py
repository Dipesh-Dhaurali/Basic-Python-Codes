"""
1
1 2
1 2 3
1 2 3 4
"""

row=4
column=4

for i in range(1,row+1):
    for j in range(1,column+1):
        if j<=i:
            print(j,end=" ")
        else:
            print(" ",end=" ")
    print()
