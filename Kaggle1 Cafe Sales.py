import pandas as pd

df = pd.read_csv(r"C:\Users\jason\Downloads\dirty_cafe_sales.csv")
#Data Cleaning
df=df.replace('UNKNOWN', '')
df=df.replace('ERROR', '')
df=df.fillna('')

#convert data types
df[['Quantity','Price Per Unit','Total Spent']]=df[['Quantity','Price Per Unit','Total Spent']].replace('','0')
df['Quantity']=df['Quantity'].astype(int)
df['Price Per Unit']=df['Price Per Unit'].astype(float)
df['Total Spent']=df['Total Spent'].astype(float)



