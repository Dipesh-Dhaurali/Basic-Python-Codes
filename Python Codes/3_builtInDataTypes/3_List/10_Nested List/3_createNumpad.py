"""
https://youtu.be/Xy6qeQWQwFw

Bro Code(Python 2D collections are easy) (cont...) (6:14)

"""
# creating the numpad of a phone using nested list

number=[
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ["*",0,"#"]
    ]

for key in number:
    for value in key:
        print(value,end=" ")
    print()

