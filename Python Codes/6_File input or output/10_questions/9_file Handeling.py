"""
book pg (143)
"""
#WAP to handling a error:
try:
    with open('demo.txt','r') as file:
        text=file.read()
        print(text)
except FileNotFoundError:
    print("Error: File not found.")

