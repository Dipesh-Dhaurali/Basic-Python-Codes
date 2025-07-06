"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
row=5
column=5

for i in range(1,row+1):
    k=6-i
    for j in range(1,column+1):
        if j<=6-i:
            print(k,end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()