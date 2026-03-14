#Factorial series using recursion       # 5! = 5*4*3*2*1*1 = 5*4! = n*(n-1)
def fact(n):
    if n<=1: #base case
        return 1
    else:
        return n*fact(n-1) #recursive case

fat=fact(5)
print(fat)





# Factorial series normal
# def fact(n):
#     if n<0:
#         print("Factorials are not defined for negative numbers")
#
#     result=1
#     for i in range(1,n+1):
#         result*=i
#     return result
#
# f=fact(5)
# print(f)
