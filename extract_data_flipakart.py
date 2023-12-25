import requests
import pandas as pd
from bs4 import BeautifulSoup
names=[]
prices=[]
des=[]
reviews=[]
for i in range(1,4):
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    res=requests.get(url)
    soup=BeautifulSoup(res.text,"lxml")
    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")
    name=box.find_all("div",class_="_4rR01T")
    for i in name:
        names.append(i.text)
    cost=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for j in cost:
        prices.append(j.text)
    description=box.find_all("ul",class_="_1xgFaf")
    for k in description:
        des.append(k.text)
    rev=box.find_all("div",class_="_3LWZlK")
    for l in rev:
        reviews.append(l.text)

    print(len(reviews))
    print(len(des))
    print(len(names))
    print(len(prices))
df=pd.DataFrame({"product":names,"price":prices,"description":des,"review":reviews})
df.to_csv("mobiles.csv")