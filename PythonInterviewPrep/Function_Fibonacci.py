# fibonacci series recursion
def fibo(n):
    if n<=0:
        return 0
    elif n==1:
        return 1

    else:
        return fibo(n-1)+fibo(n-2)
# print(fibo(6)) #8
#it prints the all sequences of fibonacci
a=5
for i in range(a):
    print(fibo(i),end=" ")   #0 1 1 2 3 5 8 13 21




# normal method
# def fibo(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# fibo(5)


