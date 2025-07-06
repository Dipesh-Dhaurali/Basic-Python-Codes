"""
https://youtu.be/j2G68uQtOwM?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
CWH(#33) (4:24)
"""

#accessing through the square bracket
dict1={
    'name':'Dipesh',
     'age':21,
     'address':'kathmandu',
     'marks':[50,60,70]
}

#individual normal accessing
print(dict1['name'])
print(dict1['age'])
print(dict1['address'])
print(dict1['marks'][0])
print(dict1['marks'][1])
print(dict1['marks'][2])


print()

# individual get method accessing
print(dict1.get('name'))
print(dict1.get('age'))
print(dict1.get('address'))
print(dict1.get('marks'))
