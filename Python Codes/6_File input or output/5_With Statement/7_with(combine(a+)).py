

# write and read inside a file with withKeyword with a+(append) mode
with open('0_demo.txt', 'a+') as file:
    file.write('I am dipesh')

    print(file.read()) #nothing will print
"""
output
-------  (noting will read but because of append mode pointer will always point to last )
I am dipesh I am dipesh

"""