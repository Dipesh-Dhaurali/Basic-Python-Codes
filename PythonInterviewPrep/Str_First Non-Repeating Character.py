#Find the first non-repeating character in a string.
char = "MMaioa"
freq = {}

for i in char:
    freq[i] = char.count(i)

for i in char:
    if freq[i] == 1:
        print(i)
        break