"""
https://youtu.be/S3mgJsdwr3U

technologyCult (How to Concatenate tuples in python? | sum ) (2:27)
+
pdf (93)
"""
#method 1
# joining tuple using sum operator
num=(1,2,3,4,5)
alpha=('a','b','c')

s=sum((num,alpha),())
print(s)                  #(1, 2, 3, 4, 5, 'a', 'b', 'c')


##########################
#method 2
#making basic tuple using list of tuple with sum operator
n=[(1,2),(3,4),(5,6)]

s=sum(n,())
print(s)           #(1, 2, 3, 4, 5, 6)