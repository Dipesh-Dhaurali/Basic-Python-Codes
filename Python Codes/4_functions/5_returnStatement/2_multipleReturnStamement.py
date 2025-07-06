# write theory from pdf (26)
"""
https://youtu.be/Q2PJ-LNS3FI
Portfolio Courses(Return Multiple Values From A Function) (cont...)
"""
def calc(x,y):
    sum=x+y
    diff=x-y
    mul=x*y
    div=x/y
    return sum,diff,mul,div

a,b,c,d=calc(50,10)
print("sum: ",a)
print("diff: ",b)
print("mul: ",c)
print("div: ",d)