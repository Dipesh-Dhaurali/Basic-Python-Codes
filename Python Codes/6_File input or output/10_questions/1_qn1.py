"""
shradha khapra (#7 ) (35:23)
"""
#WAF that replace occurrences of 'Java' with 'python'
#in above file

with open('1_myfile.txt','r') as file:
    text=file.read()

new_text=text.replace('java',"python")
print(new_text)
