a=5                        #0000 0101
b=6                        #0110

#Bitwise AND                #0100 = 4
print(a & b)


#Bitwise OR                 #0111 = 7
print(a | b)

#Bitwise NOT
print(~a)                   #1111 1010 =0000 0101 +1= -6
print(~b)                   #1111 1001 = -7

#Bitwise X-OR
print(a ^ b)              #0011 = 3


#swifting bits
print(a>>1) #right shift          #0101 #_0101 #0010 =2
print(b<<1) #left shift           #0110 #0110_ #1100 =12
