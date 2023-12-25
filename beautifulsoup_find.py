import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
res=requests.get(url)
soup=BeautifulSoup(res.text,"lxml")
price=(soup.find("h4",{"class":"float-end price card-title pull-right"}))
print(price.string)
des=(soup.find("p",{"class":"description card-text"}))
print(des.string)

