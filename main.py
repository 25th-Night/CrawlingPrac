import requests

# HTTP request
# GET / HTTP/1.1
# Host: www.naver.com

res = requests.get("https://www.naver.com/")
print(res.text)

