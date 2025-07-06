# private access modifier trying to access inside class

class Students:
    __College="Morgan College"
    __Faculty="BIM"

    def __init__(self,name,age,sem,CGPA):
        self.__name=name
        self.__age=age
        self.__sem=sem
        self.__CGPA=CGPA

    def showDetails(self):
        print(
            f" name={self.__name} age={self.__age} "
            f"College={self.__College} faculty={self.__Faculty} "
            f"sem={self.__sem} CGPA={self.__CGPA}"
        )


dip=Students('Dipesh',20,"5th",3.9)
dip.showDetails()


#output: name=Dipesh age=20 College=Morgan College faculty=BIM sem=5th CGPA=3.9

"""
Note:
We are trying to access the private access modifier inside the class so 
it works
"""