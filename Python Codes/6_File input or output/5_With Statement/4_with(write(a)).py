
# write inside a file with withKeyword with a(append) mode
with open('0_demo.txt', 'a') as file:
    file.write('I am dipesh')


"""
output
-------  (it will add the string to the end of the file)
I am dipeshI am dipeshI am dipesh

"""