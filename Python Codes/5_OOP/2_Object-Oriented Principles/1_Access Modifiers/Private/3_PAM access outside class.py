# private access modifier trying to access outside the class

class Students:
    __College="Morgan College"
    __Faculty="BIM"

    def __init__(self,name,age,sem,CGPA):
        self.__name=name
        self.__age=age
        self.__sem=sem
        self.__CGPA=CGPA


dip=Students('Dipesh',20,"5th",3.9)
print(dip.__College)
print(dip.__name)    #it's through an error because, we try to access a
                    # private access modifier form outside the class

