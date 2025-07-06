"""
cont...
+
CWH(#33)
"""
info={
    "name":"Dipesh",
     "Age":21 ,
     "Gender":"M",
      "height":5.6,
       "marks":[98,99,100],
       "marks2":(98,99,100),
      "Bool":True,
      ("fine",'pine'):"line",
      #["fine",'pine']:"line"  # list cannot be the key because it is a mutable
}

print(info)
print(type(info)) #<class 'dict'>


"""
output
{'name': 'Dipesh', 
'Age': 21, 
'Gender': 'M', 
'height': 5.6, 
'marks': [98, 99, 100], 
'marks2': (98, 99, 100), 
'Bool': True},
('fine', 'pine'): 'line'}
"""

#note : # key can be only mutable values like tuple