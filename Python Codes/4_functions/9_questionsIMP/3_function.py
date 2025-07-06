#WAF to find the factorial of n . (n is the parameter)
# 5!=5*4!
def fact(n):
    if n<0:
        print("Factorials are not defined for negative numbers")

    result=1
    for i in range(1,n+1):
        result*=i
    return result


f=fact(5)
print(f)




