"""
Write a program to implement the Rail Fence Cipher.
"""
def Encrypt(Message, Depth):
    #pattern
    Matrix = []
    for i in range(Depth):
        row = []
        for j in range(len(Message)):
            row.append("")
        Matrix.append(row)

    #movement logic
    row=0
    direction = 1    #Move downward
    for col in range(len(Message)):
        Matrix[row][col] = Message[col]
        if row == 0:
            direction = 1
        elif row == Depth - 1: #Last Column
            direction = -1  #Move upward
        row =row + direction

#Enctryption or read
    Encryption = ''
    for j in Matrix:
        Encryption=Encryption +''.join(j)
        print(j)
    return Encryption

M = Encrypt('SOMETHINGS', 4)
print(M)
