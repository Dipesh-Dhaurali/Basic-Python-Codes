# print rectangle

row=int(input("Enter the # of rows: "))
column=int(input("Enter the # of column: "))
symbol=input("Enter the symbol : ")


for row in range(3):
    for column in range(1,10):
        print(symbol , end="")
    print()
