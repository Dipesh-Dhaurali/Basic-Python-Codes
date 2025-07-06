"""
sharadha khapra(#6) (55:04)
"""

#WAP to print all element in list
#hint use list and index as parameter


def element(list,idx):
    if idx==len(list):
        return
    print(list[idx])
    element(list,idx+1)

fruits=['apple','banana','mango','orange']
element(fruits,0)