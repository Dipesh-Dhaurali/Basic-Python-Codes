"""
cont...
"""

#search if the word "learning " exists in the file or not
# and also return  line number

count=0
with open('1_myfile.txt','r') as file:
    while file:
        text=file.readline()
        count+=1

        if 'learning' in text:
            print(f"Line num is {count}")
