import requests
import pandas as pd
from bs4 import BeautifulSoup
url="https://www.iplt20.com/auction"
res=requests.get(url)
soup=BeautifulSoup(res.text,"lxml")
table=soup.find("table",class_="ih-td-tab auction-tbl")
#print(table)
column=[]
titles=table.find_all("th")
for i in titles:
    column.append(i.text)
df1=pd.DataFrame(columns=column)
rows=table.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    row=[j.text for j in data]
    l=len(df1)
    df1.loc[l]=row
print(df1)
df1["TEAM"]=df1["TEAM"].str.replace("\n","")
df1.to_csv("extracted_ipl_table.csv")
