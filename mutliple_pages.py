import requests
import pandas as pd
from bs4 import BeautifulSoup
for i in range(2,5):
    url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    res=requests.get(url)
    print(res)
    soup=BeautifulSoup(res.text,"lxml")
    next=soup.find("a",class_="_1LKTO3").get("href")  # to ge the link
    #we need add domin in the strting of the link 
    com_next="https://www.flipkart.com"+next
    print(com_next)

