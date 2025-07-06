#make directory
import os

#check this 1_mkdir exist if not make it
if not os.path.exists('../demo'):
    os.mkdir('../demo')

#make 1_mkdir inside same path nth times
for i in range(1,11):
    os.mkdir(f"../demo/day {i}")

