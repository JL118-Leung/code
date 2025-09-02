import pandas as pd

df = pd.read_csv(r"C:\Users\jason\Downloads\dirty_cafe_sales.csv")
#Data Cleaning
df=df.replace('UNKNOWN', '')
df=df.replace('ERROR', '')
df=df.fillna('')





