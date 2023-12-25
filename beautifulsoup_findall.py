import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
res=requests.get(url)
soup=BeautifulSoup(res.text,"lxml")
price=(soup.find_all("h4",{"class":"float-end price card-title pull-right"}))
desc=(soup.find_all("p",{"class":"description card-text"}))
prices=[i.string for i in price]
description=[j.string for j in desc]
resp=zip(description,prices)
for i in resp:
    print(i)
