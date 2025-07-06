mydict = {
    'fname': 'dipesh',
    'lname': 'dhaurali',
    'age': 21
}

#print no 1
print("print no 1")
for key in mydict:
    print(key)  #gives the output of key only

#print no 2
print("\nprint no 2")
for key in mydict:
    print(mydict[key])  #gives the output of value only


# print no 3
print("\nprint no 3")
for key in mydict:
    print(key , mydict[key]) #it gives the both output (key and value)

#print no 4
print("\nprint no 4")
for key,value in mydict.items():   # the main method to print dictionary
    print(f"{key} {value}")

