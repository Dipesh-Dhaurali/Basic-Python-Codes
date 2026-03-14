# find the second-largest number in the list
arr = [10, 20, 4, 45, 99]
largest = second = arr[0]
for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i
print(second)


# built in method
a = [10, 20, 4, 45, 99]
a.sort()
s_largest = a[-2]
print(s_largest)