"""
cwh(#61)    +  cwh(#72)
https://youtu.be/-KsfUaQEY9Y?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
"""
class Parent:
    def __init__(self):
        self.lastname = 'Dhaurali'
        self.language = 'Nepali'
        self.religion = 'Hindu'

    def showParent(self):
        print(self.lastname,self.language,self.religion)


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.lang = 'English'
        self.education='degree_pass'
        self.technology='computer_knowledge'

    def showChild(self):
        print(self.lang,self.education,self.technology)


#parent obj
p=Parent()
p.showParent()


#child obj
c=Child()
c.showChild()
c.showParent()








"""
note:
When a class derived from the another class.
The child class will inherit all the public and protected
properties and method form the parent class.

In addition , It can have its own properties and methods,
this is called as inheritance


Types of Inheritance:-
1) Single inheritance
2) Multiple inheritance
3) Multilevel inheritance
4) Hierarchical inheritance
5) Hybrid inheritance

"""