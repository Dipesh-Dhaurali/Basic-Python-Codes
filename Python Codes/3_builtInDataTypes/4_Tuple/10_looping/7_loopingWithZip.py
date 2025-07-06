"""
https://youtu.be/qj-V2Ep4coY
Telusko(Zip Function in Python) (3:05)
"""

# zip function with using loop for tuple   (we need zip loop to join it)

t1=(1,2,3)
t2=(4,5,6)
t3=zip(t1,t2)

for (a,b) in t3:
    print(a,b)