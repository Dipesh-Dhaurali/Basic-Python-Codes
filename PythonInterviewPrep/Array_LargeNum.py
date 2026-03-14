# Array the largest Number (manual)
numbers = [10, 45, 2, 99, 31, 56]
largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
print(largest)




###########
# built in method
numbers = [10, 45, 2, 99, 31, 56]
largest = max(numbers)
print(largest)
