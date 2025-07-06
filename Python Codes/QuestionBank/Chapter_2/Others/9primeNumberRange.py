#find prime number between 10-30

for i in range(10,31):
        for j in range(2,i):
                if i%j==0:
                    break
        else:
            print(i)