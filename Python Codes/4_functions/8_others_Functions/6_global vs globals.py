"""
telusko (cont...)
"""
#globals will give all the global variable from outside of functions

x = 10
y = 20

def show_globals():
    print(globals()['x']) #10

show_globals()
