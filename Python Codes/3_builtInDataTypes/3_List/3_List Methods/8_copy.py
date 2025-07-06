"""
Codewithharry (# 23 / 100) (4:44) (2_List Methods in Python)
https://youtu.be/scWc3F8LbOo?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&t=284


"""

lst=[1,2,3,4,5,6]
l=lst
l[0]=10 #[10,2,3,4,5,6]
print(lst) #[10, 2, 3, 4, 5, 6]
# even though I don't change in lst but due to same memory reference it will change the list so it is not recommended to do this in python



list1=[1,2,3,4,5,6]
ll=list1.copy()
ll[0]=10
print(list1) #[1, 2, 3, 4, 5, 6]
#it is also called sallow copy it does not change the original one if i change to the reference list


