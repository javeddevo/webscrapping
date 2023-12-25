import requests
url="https://www.flipkart.com"
res=requests.get(url)
print(res.status_code)
