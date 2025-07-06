"""
https://youtu.be/YlY2g2xrl6Q

bro Code (Learn Python LIST COMPREHENSIONS in 10 minutes!)
"""
numbers=[1,-6,-2,3,-1,6,-5,-3,8]

#get positive number
pos_num=[i for i in numbers if i>=0]
print(pos_num)

#get negative number
neg_num=[i for i in numbers if i<0]
print(neg_num)

#get even number
evn_num=[i for i in numbers if i%2==0]
print(evn_num)

#get odd number
odd_num=[i for i in numbers if i%2!=0]
print(odd_num)

