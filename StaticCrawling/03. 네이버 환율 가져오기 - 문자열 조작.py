# ---  네이버 환율 가져오기  ------------


import requests as req

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
res = req.get(url)

html = res.text

# 문자열 위치(position) 확인
# find 메서드는 실제 크롤링할 때 쓰이기보다는
# 이 페이지, 문자열에서 원하는 문자가 있는지 여부를 확인할 때 사용
pos = html.find("미국 USD")
print(pos)                      # 1076

usd = html.split('<span class="value">')[1].split("</span>")[0]
print(usd)                      # 1,294.00