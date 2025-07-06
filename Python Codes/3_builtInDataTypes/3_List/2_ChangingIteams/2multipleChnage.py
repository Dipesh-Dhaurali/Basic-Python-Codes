# follow pdf slide no 48
# video ( Neso Academy )=> (Changing 2_List Items in Python)
# link  ( https://youtu.be/KuyPs2zP8Uo )


#example 1

list1=[0,1,2,3,4,5,6,7]
# list1=[0,_,_,_,4,5,6,7]

list1[1:4]=[10,11,12]   #output [0, 10, 11, 12, 4, 5, 6, 7]       #note it change the value up to the 3rd index as we have given the 4th index so it means (4-1)=3rd index
print(list1)

list1[5:]=["end"]  #output   [0, 10, 11, 12, 4, 'end']          #note while updating with slicing [] big brackets are compulsory
print(list1)




#example 2

fruits=["Manggo","Banana","Grapes"]
print(fruits)       #['Manggo', 'Banana', 'Grapes']
#updating the list
fruits[:]=["Apple","Pineapple","papaya"]
print(fruits)        #['Apple', 'Pineapple', 'papaya']
