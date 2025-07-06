# Print numbers from 100 to 1 .

#while loop
i=100
while i>=1:                 #note ( start value is from 100 )
    print(i)                   #note ( always use greater than )
    i-=1                        # note ( always use decrement to print reverse)

# #for loop
# for i in range(100,0,-1):   # note ( start value is form 100)
#     print(i)                # note ( end value is (n-1) (1-1) s0 0)
#     i-=1

"""
note:
Here , Step size is compulsory because default 
step size is 1 and with out giving the step size 
the code understand the step size is 1 which 
is only used for positive pricing not for 
reverse printing so we need to give the step size (-1)
 
"""

