#write a program to return vowel letter from the file with its index
with open('1_myfile.txt', 'r') as file:
    text = file.read()

for key, val in enumerate(text):
    if val in 'aeiou':
        print(f"Vowel '{val}' found at index {key}")
