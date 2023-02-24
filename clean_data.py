import pandas as pd
import csv

df = pd.read_csv("final_star_data.csv")
#print(df.columns)

df.drop(["Unnamed: 0","luminousity","Unnamed: 6","Star_name","Distance","Mass","Radius"],axis = 1, inplace=True)
#print(df)

final_data = df.dropna()
final_data.reset_index(drop=True,inplace = True)
print(final_data)

final_data.to_csv("final_star_data.csv")