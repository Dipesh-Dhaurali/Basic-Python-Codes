"""
cont... (9:32)
"""

dict1={
    'name':'Dipesh',
     'age':21,
     'address':'kathmandu',
     'marks':[50,60,70]
}

#since dictionary are mutable so it can be changed

dict1['name']='Kritika'  #update
dict1['address']='Dang'
dict1['fev_col']=('white','black','blue') #since it is not exist so it will add to the last of the dict


print(dict1)
#{'name': 'Kritika', 'age': 21, 'address': 'Dang', 'marks': [50, 60, 70], 'fev_col': ('white', 'black', 'blue')}
