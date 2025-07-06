# create an CSV file
import pandas as pd

dict1={
    'name':['dipesh','hari','kritika'],
    'marks':[92,14,90],
    'city':['chitwan','pokhara','dang']
}

df=pd.DataFrame(dict1)
df.to_csv('friends.csv')
