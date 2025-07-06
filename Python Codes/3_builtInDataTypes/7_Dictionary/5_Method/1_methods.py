"""
https://youtu.be/078tYSD7K8E?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&t=863
sharada cont...(14:23)

+


"""

student={
    'name':'Dipesh',
    'Age':21,
    'address':'kathmandu',
    'height':5.6
}

#find the length of student dict
print(len(student))   #4 (it will find the total number of keys)



#  key method (to get all keys of dict)
print(student.keys())   #dict_keys(['name', 'Age', 'address', 'height'])



#values method  (to get all values of dict)
print(student.values())  # #dict_values(['Dipesh', 21, 'kathmandu', 5.6])



# items method (to get all key and value paris as a tuple)
print(student.items()) #dict_items([('name', 'Dipesh'), ('Age', 21), ('address', 'kathmandu'), ('height', 5.6)])



# get method (returns the key according to the value)
print(student.get('name'))  #Dipesh  #replace of student['name']





##################################################
#update method (insert the specified items to the dictionary)

# 1) change
student.update({'height':5.8})   #replace of student['height':5.8]

# 2) add new value
student.update({'weight':75})     #replace of student['weight':75]

print(student)
#{'name': 'Dipesh', 'Age': 21, 'address': 'kathmandu', 'height': 5.8, 'weight': 75}