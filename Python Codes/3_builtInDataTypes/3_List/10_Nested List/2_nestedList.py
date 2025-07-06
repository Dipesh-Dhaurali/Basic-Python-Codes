"""
https://youtu.be/Xy6qeQWQwFw

Bro Code(Python 2D collections are easy)
"""

#nested  list
foods=[
    ["Apple","Banana","Orange","Mango"],
    ["Potato","Cabbage","Cauliflower"],
    ["Chicken","Fish","Egg"]
]

#accessing with nested loop
for key in foods:
    for value in key:
        print(value,end=" ")
    print()


#accessing with single loop
for key in foods:
    print(key)

#write both output
