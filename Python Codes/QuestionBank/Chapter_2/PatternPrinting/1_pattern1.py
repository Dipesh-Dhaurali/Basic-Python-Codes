"""
*
* *
* * *
* * * *
"""
row=4
column=4

for i in range(1,row+1):
    for j in range(1,column+1):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

