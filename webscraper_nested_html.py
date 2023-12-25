import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
res=requests.get(url)
soup=BeautifulSoup(res.text,"lxml")
box=soup.find_all("div",class_="col-md-4 col-xl-4 col-lg-4")[2]

price=box.find("a").text
print(price)
