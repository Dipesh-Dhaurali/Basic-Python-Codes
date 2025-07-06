"""
sharadha khapra (cont...#6) (19:07)
+
telusko(cont..)
"""
#follow pdf slide no 11
# write theory 1st

# Assigning a default value to parameter,which is used when no argument is passed


#example 1 both argument is default
def product(a=2,b=3):
    mul= a*b
    print(mul)

product() #6


#example 2 single argument is default
def product(a,b=3):
    mul= a*b
    print(mul)

product(1) #3


#example 3 single argument is default
"""
def product(a=1,b):
    mul= a*b
    print(mul)

product(3) 

it throws an error because non default argument should be in first
and default argument will be in second

"""
# right way to do this is below
def product(b,a=1):
    mul= a*b
    print(mul)

product(4) #4
