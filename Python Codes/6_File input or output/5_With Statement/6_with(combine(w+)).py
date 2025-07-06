
# write and read inside a file with withKeyword with w+ mode
with open('0_demo.txt', 'w+') as file:
    file.write('I am dipesh')

    print(file.read())  #nothing will print


"""
output  
------ (noting will read but because of write mode it will overwrite all file text)
i am dipesh
"""