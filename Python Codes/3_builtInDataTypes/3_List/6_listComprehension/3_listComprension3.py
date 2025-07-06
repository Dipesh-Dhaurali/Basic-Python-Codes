"""
https://youtu.be/eF6nK5bSlmg?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
CodeWithHarry (Introduction to Lists in Python #22)    (17:20)
"""
# make a list of number having element value 1 to 10 using list comprehension

list1=[i for i in range(1,11)]
print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# make a list of number having element value is square of list from 1 to 10
# using list comprehension

list2=[i*i for i in range(1,11)]
print(list2)

#print only even number from the square of 1 to 10
list3=[i*i for i in range(1,11) if i%2==0]
print(list3)