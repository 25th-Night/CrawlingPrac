import requests as req
import re

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text

# r : 정규표현식 객체를 생성
# pattern : '미국 USD' + 아무문자나 0개 이상 + 'value">' + (.*)로 캡쳐 + '</' 로 끝남
# . : 개행(줄바꿈)을 제외한 모든 문자
r = re.compile(r"미국 USD.*value\">(.*)</")
captures = r.findall(body)

print(captures)
# []    <- 개행 문자를 포함하지 못해서 인식을 못한 것임


# ---------------------------------------------
print("---------------------------------------")


r = re.compile(r"미국 USD.*value\">(.*)</", re.DOTALL)
captures = r.findall(body)

print(captures)
# ['80855.09</span>\n\t\t\t\t\t\t\t<span class="txt_krw"> ...]
# 원하는 결과가 나오지 않음
# 미국 USD 뒤에 ".*" 가 말그대로 아무문자나 0개 이상을 의미하기 때문
# 제일 마지막에 나오는 "value>" 까지 포함시키게 됨
# 그 이후에 쭊 내려가서 가장 마지막에 나오는 "</" 까지 가져옴


# ---------------------------------------------
print("---------------------------------------")


# ? : 가장 좁은 범위로 선택
r = re.compile(r"미국 USD.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print(captures)
# ['1,312.00']


# ---------------------------------------------
print("---------------------------------------")


# 통화명과 환율을 짝을 맞춰 모두 찾아오기
r = re.compile(r"blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print(captures)
# [('미국 USD', '1,312.00'), ('원', '912.73'), ('원', '1,429.29'), ('원', '181.84'), ('원', '143.7400'), ('엔', '1.0880'), ('달러', '1.2707'), ('달러', '102.5400'), ('상승', '69.16'), ('달러', '1572.97'), ('원', '1929.6'), ('달러', '80855.09')]
# 뭔가 제대로 조회가 되지 않고 있음.


# ---------------------------------------------
print("---------------------------------------")


# span 태그를 감싸고 있는 h3 태그까지 함께 활용하여 조회
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)
captures = r.findall(body)

print(captures)
# [('미국 USD', '1,312.00'), ('일본 JPY(100엔)', '912.73'), ('유럽연합 EUR', '1,429.29'), ('중국 CNY', '181.84'), ('달러/일본 엔', '143.7400'), ('유로/달러', '1.0880'), ('영국 파운드/달러', '1.2707'), ('달러인덱스', '102.5400'), ('WTI', '69.16'), ('휘발유', '1572.97'), ('국제 금', '1929.6'), ('국내 금', '80855.09')]
# 원하는 바대로 조회가 되었음.


# ---------------------------------------------
print("---------------------------------------")

# 환율 계산기로 출력되도록 코딩

print()
print("환율 계산기")
print("-----------")
print()

for currency, exchange_rate in captures:
    print(f"{currency}의 환율은 {exchange_rate}원 입니다.")

print()

usd = float(captures[0][1].replace(",", ""))
won = int(input("달러로 바꾸길 원하는 금액(원)을 입력해주세요 : "))
dollar = int(won / usd)
print(f"요청하신 {won} 원은 {dollar} 달러로 환전이 됩니다.")