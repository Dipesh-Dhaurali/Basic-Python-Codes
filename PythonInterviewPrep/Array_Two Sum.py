
nums = [1, 6, 3, 9]
target = 12

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Match found: {nums[i]} and {nums[j]}")