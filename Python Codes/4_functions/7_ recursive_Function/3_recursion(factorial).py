# 5! = 5*4*3*2*1*1 = 5*4! = n*(n-1)


def fact(n):
    if n<=1: #base case
        return 1
    else:
        return n*fact(n-1) #recursive case

fat=fact(5)
print(fat)