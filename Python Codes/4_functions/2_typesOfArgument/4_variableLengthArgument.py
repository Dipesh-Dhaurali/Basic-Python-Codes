#follow pdf slide no 13
# write theory 1st
"""
telusko(Cont...)
"""
#variable length argument

def add(a, *b):
    c=a
    for i in b:
        c+=i
    print(c)

add(1,2,3,4,5,6,7,8,9,10)   #55



# variable length argument example 2 from pdf 13(self)
def person(name,*marks):
    print(f"My name is {name}",end=" ")
    total_marks=0

    for i in marks:
       total_marks+=i
    print(f"and my total marks is {total_marks}.")

person('Dipesh',90,91,92,93,94)
#output : My name is Dipesh and my total marks is 460.


"""
note
1) variable length argument will always get in the form of tuple
2) single star is compulsory for variable length argument
"""