# Count Character Frequency
#######################
char = "HelloWorld"
freq = {}
for i in char:
    freq[i] = char.count(i)
print(freq)









#######################
char="HelloWorld"
freq ={}

for i in char:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i] = 1
print(freq)

