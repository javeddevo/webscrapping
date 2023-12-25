import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
res=requests.get(url)
soup=BeautifulSoup(res.text,"lxml")
price=(soup.find_all("h4",{"class":"float-end price card-title pull-right"}))
name=soup.find_all("a",class_="title")
description=soup.find_all("p",class_="description card-text")
prices_list=[]
name_list=[]
description_list=[]
for i in name:
    n=i.string
    name_list.append(n)
for j in description:
    d=j.string
    description_list.append(d)
for z in price:
    p=z.string
    prices_list.append(p)
print(len(prices_list))
print(len(description_list))
print(len(name_list))
df=pd.DataFrame({"Product":name_list,"Price":prices_list,"Description":description_list})
df.to_csv("scrapped_data.csv")
