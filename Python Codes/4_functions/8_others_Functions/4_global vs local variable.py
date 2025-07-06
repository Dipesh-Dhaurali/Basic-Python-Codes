"""
https://youtu.be/QYUbLevwgDQ?list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3
Telusko (Global vs Local Variable)
"""
a=10

def something():
    a=15
    print("inside function",a) #15

something()
print("outside function",a) #10