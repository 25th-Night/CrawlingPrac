from bs4 import BeautifulSoup as BS
import requests as req

# python "StaticCrawling/14. webhook.site 실습.py"

# GET 요청

# url = "https://webhook.site/0603ae22-be20-4df5-8929-d265c6af8752"
# querystring = "?name=csw&message=hi"
# headers = {"User-Agent": "csw"}
# res = req.get(url + querystring, headers=headers)
# print(res.status_code)      # 200
# print(res.text)             # ""


# -----------------------------------------------


# POST 요청

url = "https://webhook.site/0603ae22-be20-4df5-8929-d265c6af8752"
data = {
    "name": "csw",
    "message": "hi"
}
res = req.post(url, data=data)
print(res.status_code)
print(res.text)