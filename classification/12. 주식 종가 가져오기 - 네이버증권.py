from bs4 import BeautifulSoup as BS
import requests as req

# python "classification/12. 주식 종가 가져오기.py"

url = "https://finance.naver.com/sise/lastsearch2.naver"
res = req.get(url)
soup = BS(res.text, "html.parser")

for title in soup.select("a.tltle"):    # class명이 title 이 아니라 tltle 임.
    print(title.get_text(strip=True))

for tr in soup.select("table.type_5 tr"):
    if len(tr.select("a.tltle")) == 0:
        continue
    title = tr.select("td a.tltle")[0].get_text(strip=True)
    price = tr.select("td.number:nth-child(4)")[0].get_text(strip=True)
    change = tr.select("td.number:nth-child(6)")[0].get_text(strip=True)
    print(title, price, change)