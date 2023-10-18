import pandas as pd

a=pd.read_csv("./dataset/covid_19_india.csv")#load the dataset
print(a.head())

a.dropna(inplace=True)
a.drop_duplicates(inplace=True)
a['Date']=pd.to_datetime(a['Date'])
a['Time']=pd.to_datetime(a['Time'],format='%I:%M %p')
a['Cured']=pd.to_numeric(a['Cured'])
a['Deaths']=pd.to_numeric(a['Deaths'])
a['Confirmed']=pd.to_numeric(a['Confirmed'])
a=a.rename(columns={'State/UnionTerritory': 'State'})
a=a[['Date','State','Cured','Deaths','Confirmed']]
a.to_csv("./dataset/new.csv",index=False)
print(a)