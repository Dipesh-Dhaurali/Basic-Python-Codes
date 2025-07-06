#check vowel exist or not if yes return its index
list1 = ['apple', 'ball', 'cat', 'dog', 'egg']
vowel = ['a', 'e', 'i', 'o', 'u']

for key, value in enumerate(list1):
    for char in value: #check each character in the word
        if char in vowel:
            print(f"pos:{key}, value:{char}")



