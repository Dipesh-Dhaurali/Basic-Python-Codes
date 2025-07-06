"""
https://youtu.be/kj850Y8y8FI
Telusko( Filter Map Reduce)
+
https://youtu.be/OErhjT4f5Cs
CWH(Map, Filter and Reduce in Python #53)
"""
#write definition of fileter and map

num=[3,4,2,6,5,7,8]


#1) filter
even=list(filter(lambda n:n%2==0,num))
print(even)  #[4, 2, 6, 8]

odd=list(filter(lambda n:n%2!=0,num))
print(odd)   #[3, 5, 7]



#2) Map = > preform inside function
double=list(map(lambda n:n*2,even))
print(double) #[8, 4, 12, 16]x

square=list(map(lambda n:n**2,num))
print(square) #[9, 16, 4, 36, 25, 49, 64]


#3) reduce
#write definition of reduce

from functools import reduce

sum=reduce(lambda a,b:a+b,double)
print(sum)  #40

add=reduce(lambda a,b:a+b,num)
print(add) #35