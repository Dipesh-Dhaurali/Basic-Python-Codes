"""
sharadha khapra(#6) (21:39)
"""
#WAF to print the length of a list . (list is the parameter)
def length_list(*lst):
    count=0
    for i in lst:
        count+=1
    print(count)

list1=[1,2,3,4,5,6,7,9]
length_list(*list1)


