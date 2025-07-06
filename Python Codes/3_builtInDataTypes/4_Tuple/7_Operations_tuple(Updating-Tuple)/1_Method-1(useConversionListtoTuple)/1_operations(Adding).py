"""
https://youtu.be/XblLSduioJI?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
CodeWithHarry (Operations on Tuples in Python #(25/100))

+

https://youtu.be/tHmIf6WU26E
Neso Academy (Updating a Tuple in Python)
"""
#Addng new items to a tuple

cars=('Audi','Mercedes','BMW')

#add (TATA)
temp=list(cars) #convert to the list
temp.append("TATA")  #append method
cars=tuple(temp)
print(cars)

#add (toyota)
temp=list(cars)
temp.insert(1,"Toyata") #insert method
cars=tuple(temp)
print(cars)

#add (Thar,Honda)
temp=list(cars)
temp.extend(["Thar","Honda"]) #extend method  (bracket is compulsory in extend method)
cars=tuple(temp)
print(cars)



