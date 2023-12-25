import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://ticker.finology.in/"
res=requests.get(url)
soup=BeautifulSoup(res.text,"lxml")
table=soup.find("table",class_="table table-sm table-hover screenertable")
header=table.find_all("th")
titles=[]
for i in header:
    titles.append(i.text)
#print(titles)
df=pd.DataFrame(columns=titles)
rows=table.find_all("tr")
# print(rows)
# print("================")
for i in rows[1:]:
    data=i.find_all("td")
    row=[tr.text for tr in data]
    # print(row)
    l=len(df)
    print(l)
    df.loc[l]=row
print(df)
df['Company'] = df['Company'].str.replace('\n', '')
df.to_csv("extrcated_table.csv")