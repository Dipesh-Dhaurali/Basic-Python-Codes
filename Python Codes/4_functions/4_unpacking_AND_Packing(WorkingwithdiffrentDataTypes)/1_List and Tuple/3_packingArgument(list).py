#followed by pdf(21)


#using packing with loop


#for the list
def fun(*data):

    for i in data:
        print(i)    #[9, 8, 7, 6]

list1=[9,8,7,6]
fun(list1)



#for the tuple
def fun(*data):

    for i in data:
        print(i)    #[9, 8, 7, 6]

tup1=(9,8,7,6)
fun(tup1)







"""
#(wrong way)
def funs(*data):
    print(data)   #([19, 18, 17, 16],)  #only gives value for a

list2=[19,18,17,16]
funs(list2)

"""