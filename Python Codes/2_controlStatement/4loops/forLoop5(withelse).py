# print the string as character and search the letter
# if letter exists then exit it

str="Hello World"
for char in str:
    if char=='W':
        print("Search letter found")
        break
    print(char)
else:
    print("Program ended")