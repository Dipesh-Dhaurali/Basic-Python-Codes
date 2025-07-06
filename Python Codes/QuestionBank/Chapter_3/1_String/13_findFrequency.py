# Write a Python program to find the frequency of each character in a string.
#example -:  banana {'b': 1, 'a': 3, 'n': 2}

string = "banana"
frequency = {}

for i in string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print(frequency)

#write this code output also