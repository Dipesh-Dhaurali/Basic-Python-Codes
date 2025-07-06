"""
https://youtu.be/JnVGh16yyGY
WsCube Tech! ENGLISH (Python 2_Dictionary Program: How to Merge Two Dictionaries?)

+
pdf (120)

"""


#combination dictionary

# unpacking to combine two dictionary
emp1={
    'name':'Ram',
    'age':30,
    'address':'pokhara',
    'weight':90

}
emp2={
    'name':'hari',
    'age':25,
    'address':'kathmandu',
    'hieght':6
}

dict1={**emp1,**emp2}
print(dict1)
#{'name': 'hari', 'age': 25, 'address': 'kathmandu', 'weight': 90, 'hieght': 6}