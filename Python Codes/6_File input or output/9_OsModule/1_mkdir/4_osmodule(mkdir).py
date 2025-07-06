#make directory
import os

#create a single 1_mkdir to particular path
path = os.path.join(r"C:\Users\DipeshDip\Desktop", "dip")
os.mkdir(path)


#create a multiple 1_mkdir inside path
for i in range(1,101):
    os.mkdir(fr"C:\Users\DipeshDip\Desktop\dip\day {i}")

