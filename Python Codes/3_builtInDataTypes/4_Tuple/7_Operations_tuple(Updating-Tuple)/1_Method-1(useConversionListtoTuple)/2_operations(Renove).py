"""
cont ...
"""

# remove operation in tuple
cars=('Audi', 'Toyota', 'Mercedes', 'BMW', 'TATA', 'Thar', 'Honda')

#1) remove Mercedes
temp=list(cars)
temp.remove('Mercedes') #remove method
cars=tuple(temp)
print(cars)

#2) remove last index (Honda)
temp=list(cars)
temp.pop() #pop method without index
cars=tuple(temp)
print(cars)

#2) remove mid-index (BMW)
# recent value = ('Audi', 'Toyota', 'BMW', 'TATA', 'Thar')
temp=list(cars)
temp.pop(2) #pop method with index
cars=tuple(temp)
print(cars)

#3) remove 'tata'
temp=list(cars)
del temp[2] #del method with index vale
cars=tuple(temp)
print(cars)

#3) remove 'multiple values'
temp=list(cars)
del temp[1:] #del method with slicing value
cars=tuple(temp)
print(cars)

#4) remove all values from  the tuple
temp=list(cars)
temp.clear() #clear method
cars=tuple(temp)
print(cars)