# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:22:14 2020

@author: Sagnik Bakshi
"""
import pandas as pd

csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df2 = pd.read_excel(xlsx_path)

x = df[['Length']]

# Viewing and accessing data
a = df['Length']

b = type(df[['Length']])

c = df[['Artist','Released','Genre']]

d = df.iloc[0:3,0:4]

q=df[['Rating']]

q=df[['Released','Artist']]

r = df.iloc[1,2]

