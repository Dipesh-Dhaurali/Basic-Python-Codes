#Create a list of strings that only contain words that start with a
# vowel from a given list.
list1=["ram","europe","raju","umbrella","orange","shyam"]
#euripe,umbrella,orange
list2=[i for i in list1 if i[0] in "aeiou"]

print(list2)
