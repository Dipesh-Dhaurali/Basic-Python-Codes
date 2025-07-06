'''
>=90% => 4 GPA   => Excellent (A-)
>=80% => 3.6 GPA => Distinction  (A)
>=70% => 3.2 GPA =>First Division (B+)
>=60% => 3.0 GPA =>Second Division (B)
>=50% => 2.8 GPA =>Third Division (B-)
<50   => NG      => Fail (F)

'''
mark=float(input("Enter your marks "))

if mark>=90:
    print(" 4 GPA\n Excellent \n A- Grade ")
elif mark>=80 and mark<90:
    print(" 3.6 GPA\n Distinction \n A Grade ")
elif mark>=70 and mark<80:
    print(" 3.2 GPA\n First Division \n B+ Grade ")
elif mark>=60 and mark<70:
    print(" 3.0 GPA\n Second Division \n B Grade ")
elif mark>=50 and mark<60:
    print(" 2.8 GPA\n Third Division \n B- Grade ")
else:
    print("Fail")
