"""
https://youtu.be/lDXqspXV9pA
Bek Brace (**KWARGS used in dictionaries for packing and unpacking arguments)
"""
#method 1
def info(name,age,country):
    print(name,age,country)



dict1={
    'name':'dipesh',
    'age':21,
    'country':'Nepal'
}

info(**dict1)

#####################
# method 2
def info(name, age, country):
    return name, age, country


a, b, c = info(name='dipesh', age=21, country='Nepal')
print(a, b, c)
###################################################

#method 3
def info(name,age,country):
   print(name,age,country)


info(name='dipesh',age=21,country='Nepal')

#################################################
#method 4
def info(name,age,country):
    for key,val in locals().items():
        print(key,val)
info(name='dipesh',age=21,country='Nepal')

#########################################
