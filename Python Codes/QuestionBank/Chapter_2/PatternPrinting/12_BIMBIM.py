"""
BIMMIB
IMMI
MM

"""


# row = 3
# column = 6
# symbols = "BIMMIB"
#
# for i in range(row):
#     # Each row needs to print symbols starting from the i-th character
#     for j in range(i, column):
#         if j < column - i:  # print only the characters until the required length for the row
#             print(symbols[j], end="")
#         else:
#             print(" ", end="")
#     print()



value="BIM"

for i in range(3):
    str=""
    rev=""
    a=value
    for x in a:
        str=str+x
        rev=x+rev
    value=""
    for j in a:
        if j==a[0]:
            continue
        value=value+j
    print(str+rev)