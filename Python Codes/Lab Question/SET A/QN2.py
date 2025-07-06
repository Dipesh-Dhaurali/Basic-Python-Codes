"""
Read a CSV file into a Pandas DataFrame,
handle missing data, and perform basic
data manipulation (filtering, subsetting).
"""
import pandas as pd

df = pd.read_csv('data.csv')
df.columns = df.columns.str.strip()
print("Original CSV File \n ",df)


cls = df.dropna()
print("\n Handling missing values \n ",cls)


fltr = cls[cls['score'] > 95]
print("\n filter rows \n ",fltr)


subset = cls[['name', 'score']]
print("\n subset \n ",subset)
