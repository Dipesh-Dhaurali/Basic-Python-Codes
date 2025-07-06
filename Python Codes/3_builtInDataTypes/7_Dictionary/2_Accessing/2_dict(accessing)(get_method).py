#accessing through the get method


dict1={
    'name':'Dipesh',
     'age':21,
     'address':'kathmandu',
     'marks':[50,60,70]
}


print(dict1.get('height')) #None      #even though it is not exist in the dict1, but it doesn't through error
# print(dict1['height']) #it throws error because it is not exist in the dictionary