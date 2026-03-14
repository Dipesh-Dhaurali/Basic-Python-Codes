words = ["apple", "banana", "cherry", "strawberry"]
longest = words[0]

for i in words:
    if len(i) > len(longest):
        longest = i

print(longest)