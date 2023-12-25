import requests
from bs4 import BeautifulSoup
url="https://webscraper.io/test-sites/e-commerce/allinone/computers"
res=requests.get(url)
# print(res.text)
soup=BeautifulSoup(res.text,"lxml")
# print(soup)
tags=soup.div  # tehre are differebt tags like hearder ul div...
print(tags)
attributes=tags.attrs
print(attributes)