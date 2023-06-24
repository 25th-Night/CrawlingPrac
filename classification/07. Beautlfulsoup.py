from bs4 import BeautifulSoup as BS
import requests as req


url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)

soup = BS(res.text, "html.parser")

tds = soup.find_all("td")
print(tds)
# 원하는 결과가 나오지 않음


url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)

soup = BS(res.text, "html.parser")

tds = soup.find_all("td")

names = []
for td in tds:
    if len(td.find_all('a')) == 0:
        continue
    names.append(td.get_text(strip=True))

prices = []
for td in tds:
    if "class" in td.attrs and "sale" in td.attrs["class"]:
        prices.append(td.get_text(strip=True))

print(names)
print(prices)

for name, price in zip(names, prices):
    print(name, price)