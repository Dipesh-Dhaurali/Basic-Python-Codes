# print a number 1 to 10 using while loop

i=1
while i<=10:
    print(i)
    i=i+1
    if i==5:
        break
else:
    print("Loops ended")

#note
# if i stops the code prematurely with break
# statement the else case will not executed
# so , in this case else will never run