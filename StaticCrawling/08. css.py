from bs4 import BeautifulSoup as BS
import requests as req


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


# -- css를 이용하여 환율을 가져오는 코드 개선 ----------
print("-- css를 이용하여 환율을 가져오는 코드 개선 ----------")

# find_all 대신 select 메서드를 사용

names = []
for td in soup.select("td.tit"):
    names.append(td.get_text(strip=True))

prices = []
for td in soup.select("td.sale"):
    prices.append(td.get_text(strip=True))

for name, price in zip(names, prices):
    print(name, price)