#updaing tuple using slicing

tup1=('apple','ball','cat','dog','fish')

#add cherry after the cat
tup2=tup1[:3] +('cherry',)+tup1[3:]
print(tup2)


#replace ball with banana
#('apple', 'ball', 'cat', 'cherry', 'dog', 'fish')
tup3=tup1[:1]+('banana',)+tup1[2:]
print(tup3)

#note don't miss comma otherwise the error occurs
#slicing last value start from 0 and works on (n+1)