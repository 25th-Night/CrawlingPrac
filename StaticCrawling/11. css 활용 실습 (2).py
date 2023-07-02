
#  ---  쿠팡 크롤링 (광고 제외)  -------

# python "StaticCrawling/11. css 활용 실습 (2).py"

from bs4 import BeautifulSoup as BS
import requests as req

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
}
res = req.get(url, headers=headers)
soup = BS(res.text, "html.parser")

arr = [a.get_text(strip=True) for a in soup.select('div.name')]


for desc in soup.select("div.descriptions-inner"):
    ads = desc.select("span.ad-badge")
    if len(ads) > 0:
        print("광고!")
    print(desc.select_one("div.name").get_text(strip=True))