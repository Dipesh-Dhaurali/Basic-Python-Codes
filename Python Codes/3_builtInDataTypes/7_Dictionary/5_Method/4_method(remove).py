"""
codeWithHarry(Cont....) (3:25)
"""
emp1={
    'name':'Ram',
    'age':30,
    'address':'pokhara'
}
#pop method (to delete values and keys from dict)
emp1.pop('age')
print(emp1)   #{'name': 'Ram', 'address': 'pokhara'}


#popiteam method   (delete the last key and value of dict)
emp1.popitem()
print(emp1)   #{'name': 'Ram'}


#del key (to delete the key value paris)
del emp1['name']
print(emp1)  #{}


#del key (to delete entire dictionary with their variable name)
del emp1
#print(emp1) #error because emp1 doesnt exist as variable