# set method
nums = [1, 2, 2, 3, 4, 4, 4, 5]
rem = list(set(nums))
print(rem)




# normal method
num = [5, 1, 2, 1, 5, 3]
new = []
for i in num:
    if i not in new:
        new.append(i)
print(new)
