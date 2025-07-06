# reverse the string with while loop
str1 = "MorganCollege"
rev = ""
i = len(str1) - 1

while i >= 0:
    rev =rev + str1[i]
    i =i- 1

print(rev)
