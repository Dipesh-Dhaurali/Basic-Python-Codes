# find the total marks of student using tuple (packing)

def mark(*mrk):
    score=0
    for i in mrk:
        score+=i
    percentage=score/len(mrk)
    print(f"My total score is {score} and my percentage is {percentage}")


mark(98,99,96,81,92)




#find the total marks of student using tuple (Unpacking)

def marks(python,AI,Marketing,SDD,IS):
    return python+AI+Marketing+SDD+IS

num=(100,85,80,90,95)
scr=marks(*num)
prt=scr/len(num)
print(f"My total score is {scr} and my percentage is {prt}")
