"""
https://youtu.be/fsAzeNZXvkE?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
telusko(pass list to a function #37)
+
https://youtu.be/0d6b6fFuCkE?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
CWH (#21)
"""
# find the odd number and even number count using function with list

def count(list1):
    even=0
    odd=0

    for i in list1:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd


list1=[10,11,20,21,30,40,41,50,60,70,43]
a,b=count(list1)   #tuple unpacking and packing

print(f"Even number count is : {a} and Odd number count is : {b}")


