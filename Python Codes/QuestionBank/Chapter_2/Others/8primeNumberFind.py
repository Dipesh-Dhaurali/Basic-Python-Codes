#find all prime number between two numbers given by user
a = int(input("Enter the start number : "))
n = int(input("Enter the end number : "))


for i in range(a, n + 1):
    if i>1:
        for j in range(2, i):
            if i % j == 0:
                break

        else:
            print(i)




