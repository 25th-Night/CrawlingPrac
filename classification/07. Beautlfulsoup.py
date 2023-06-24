from bs4 import BeautifulSoup as BS
import requests as req


url = "https://naver.com"
res = req.get(url)

title = res.text.split("<title>")[1].split("</title>")[0]
print(title)
# NAVER

soup = BS(res.text, "html.parser")
print(soup.title)
# <title>NAVER</title>

print(soup.title.string)
# NAVER
