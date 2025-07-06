"""
A
B A
C B A
D C B A

"""
row=4
column=4

for i in range(1,row+1):
    k=ord('@')+i
    for j in range(1,column+1):
        if j<=i:
            print(chr(k),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()