#Retrive the index number or break it while the vowel
#is arrived in string

strs = "I am Dipesh Dhaurali".lower()
vowels = ['a', 'e', 'i', 'o', 'u']
index = 0

for char in strs:
    if char in vowels:
        print(f"'{char}' found at index {index}")
        # break
    index += 1


