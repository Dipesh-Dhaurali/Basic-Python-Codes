# we can only make a set of immutable dataTypes
# like ( boolean , int , float , str , tuple )

set1={True,1,2.5,"hello",(1,2,3),1}
print(set1)



#it cannot be dictionary and list
set2={[1,2,3],{"name":"dipesh"}}
print(set2)
# it gives us error
"""
    set2={[1,2,3],{"name":"dipesh"}} 
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
"""