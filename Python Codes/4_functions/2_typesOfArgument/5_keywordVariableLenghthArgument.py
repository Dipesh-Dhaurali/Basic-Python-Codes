"""
https://youtu.be/kB829ciAXo4
telusko(Keyword Variable Length Arguments in Python | **kwargs)
"""
#keywords variable length argument (kwargs)
# theory from chatgpt

def person(name,**data):
    print(f"My name is {name} and my data are :")

    for key,val in data.items():
        print(f"{key}:{val}")

person('Dipesh',age=23,address='Kathmandu',phone=9821187137)



""""
note:
1) double star is compulsory for kwargs
2) variable length argument should have keyword inside it (age=23)

"""