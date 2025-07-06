"""
Shradha Khapra(#9/9) (6:25)
"""
class Account:
    def __init__(self,accNo,psw):
        self.__accNo=accNo
        self.__psw=psw

    def showdb(self):
        print(self.__accNo , self.__psw)
a=Account('224350','dipesh')
#print(a.__psw)         #it gives error because password is crucial so we use PAM at that time
a.showdb()
