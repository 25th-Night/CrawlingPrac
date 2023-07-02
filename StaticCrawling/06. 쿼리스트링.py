import requests as req

url1 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B0%90%EC%9E%90"
res1 = req.get(url1)

print(res1.text)

url2 = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=감자"
res2 = req.get(url2)

print(res2.text)