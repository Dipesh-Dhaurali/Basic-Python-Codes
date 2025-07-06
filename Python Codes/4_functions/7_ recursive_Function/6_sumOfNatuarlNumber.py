"""
sharadha khapra(#6) (55:04)
"""

#WARF to calculate the sum of first n natural number
# 5 = 1 2 3 4 5

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(5))