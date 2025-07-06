"""
cwh(#62)
+
https://youtu.be/43FK20rWvKQ?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
"""
# any instance variable in a class followed by self is a public access
# modifier that can be access in inside and outside the class

class Student:
    def __init__(self):
        self.name='dipesh'


s=Student()
print(s.name)
