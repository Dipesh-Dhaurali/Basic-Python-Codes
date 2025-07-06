mylist=[5,2,3,6,4,8]

#By default, it will sort in ascending order
mylist.sort()
print(mylist) # [2, 3, 4, 5, 6, 8]

#Decending Order
mylist1=[5,6,3,9,4,8]
mylist1.sort(reverse=True)
print(mylist1) # [9, 8, 6, 5, 4, 3]

#Accending Order
mylist1.sort(reverse=False)
print(mylist1) #[3, 4, 5, 6, 8, 9]




#######################################################





#practise sets example
mylist2=['e','z','i','k','b','a','n','q']

mylist2.sort(reverse=False)
print(mylist2) # ['a', 'b', 'e', 'i', 'k', 'n', 'q', 'z']

mylist2.sort(reverse=True)
print(mylist2) # ['z', 'q', 'n', 'k', 'i', 'e', 'b', 'a']

mylist2.sort()
print(mylist2) # ['a', 'b', 'e', 'i', 'k', 'n', 'q', 'z']
