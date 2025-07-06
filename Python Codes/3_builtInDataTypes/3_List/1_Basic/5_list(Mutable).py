"""
shrada(cont..)
"""
# list are mutable so they can be changed
student=['Dipesh',98.7,21,"Kathmandu"]

student[0]="Krtika"
student[1]=97.7
student[3]="Dang"

print(student) #output ['Krtika', 97.7, 21, 'Dang']






# note after updating the value it will replace the old one with one so
# if we try to access list now we will see the updated values





#accessing through list
for i in student:
    print(i,end=" ")  # output   # Krtika 97.7 21 Dang

