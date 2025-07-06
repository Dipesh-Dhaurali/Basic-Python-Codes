names=['Rita','Kritika','Rekha','Gita','Ram','Hari']
n=[]

#normal way
for i in names:
    n.append(i)

print(n)  #['Rita', 'Kritika', 'Rekha', 'Gita', 'Ram', 'Hari']


#list compression
nme=[i for i in names]
print(nme)
