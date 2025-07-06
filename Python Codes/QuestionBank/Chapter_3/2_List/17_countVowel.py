#Count how many times a vowel letters appears in the list.
list1=['apple','ball','cat','dog','egg']
vowel=['a','e','i','o','u']
count=0

for i in list1:
    for j in vowel:

        if j in i:
            count+=1

print(count)

