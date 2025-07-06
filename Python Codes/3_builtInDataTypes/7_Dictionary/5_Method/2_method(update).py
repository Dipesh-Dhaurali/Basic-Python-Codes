"""
https://youtu.be/LmbFwaLjT9k?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
CWH(34)
+pdf (120)
"""
# update method to combine two dictionary
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


#update method
emp1.update(emp2)
print(emp1)         #{'name': 'hari', 'age': 25, 'address': 'kathmandu', 'weight': 90, 'hieght': 6}
print(emp2)         #{'name': 'hari', 'age': 25, 'address': 'kathmandu', 'hieght': 6}

#clear method
emp2.clear()
print(emp2)          #{}

