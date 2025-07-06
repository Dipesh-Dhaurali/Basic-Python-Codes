tup1=['a','b','c','d','e','f','g','h','i','j']

print(tup1[::1]) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(tup1[::2]) #['a', 'c', 'e', 'g', 'i']
print(tup1[::3]) #['a', 'd', 'g', 'j']

print(tup1[3:8:2])#['d', 'f', 'h']

#reverse the tuple using step
print(tup1[::-1]) #['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
print(tup1[len(tup1)::-1]) #['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
