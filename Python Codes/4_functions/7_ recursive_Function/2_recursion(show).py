"""
cont...(sharadha)
"""
def show(n):

    if n==0: #base case
        return 1

    else:
        print(n ,end=" ")  #5 4 3 2 1
        return show(n-1) # recursive case

show(5)

