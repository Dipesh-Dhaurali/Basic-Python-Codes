#pdf ()
# Fibonacci
# 0 1            1 2 3 5 8 13 .... f(n-1)+f(n-2)

def fibo(n):
    if n<=0:
        return 0
    elif n==1:
        return 1

    else:
        return fibo(n-1)+fibo(n-2)

#it gives the term of the sequence
print(fibo(6)) #8


#it prints the all sequence of fibonacci
a=9
for i in range(a):
    print(fibo(i),end=" ")   #0 1 1 2 3 5 8 13 21


