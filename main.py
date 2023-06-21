# # 별칭을 사용하여 라이브러리 임포트
# import requests as req

# res = req.get('https://api64.ipify.org/')
# print(res.status_code)            # 200
# print(res.text)                   # 175.117.84.242
# print(res.raw)                    # <urllib3.response.HTTPResponse object at 0x000001A3AF6F49D0>

# # 응답 받은 것에 대한 request
# print(res.request.method)         # GET
# print(res.request.headers)        
# # {'User-Agent': 'python-requests/2.31.0', 
# # 'Accept-Encoding': 'gzip, deflate', 
# # 'Accept': '*/*', 'Connection': 'keep-alive'}

# print(res.cookies)                # <RequestsCookieJar[]>
# print(res.elapsed)                # 0:00:17.105375



# ---  문자열 메서드 : find, split  -------------


# s = 'apple'

# print(s.find('e'))

# # array
# arr = s.split('p')

# print(arr)


# ------------------

# s = '제 생일은 9월 입니다'

# print(s.find('생'))
# print(s.find('생일은'))


# ------------------

# # 문자열 내에서 특정 문자열 다음 글자 가져오기

# s = '제 생일은 9월 입니다'

# # 공백을 포함한 문자열을 가져와 위치를 확인
# pos = s.find('생일은 ')
# # 문자열의 길이만큼 덧셈
# pos += 4
# # 해당 길이에 대한 문자열 추출
# # 인덱싱이 아닌 슬라이싱으로 가져오기
# print(s[pos:pos+1])


# ------------------

# s = '제 생일은 10월 입니다'

# arr = s.split('생일은 ')
# s1 = arr[1]

# arr2 = s1.split('월')
# print(arr2)

# bd = s.split('생일은 ')[1].split('월')[0]
# print(bd)


# ---  네이버 환율 가져오기  ------------


# import requests as req

# url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
# res = req.get(url)

# html = res.text

# # 문자열 위치(position) 확인
# # find 메서드는 실제 크롤링할 때 쓰이기보다는
# # 이 페이지, 문자열에서 원하는 문자가 있는지 여부를 확인할 때 사용
# pos = html.find("미국 USD")
# print(pos)                      # 1076

# usd = html.split('<span class="value">')[1].split("</span>")[0]
# print(usd)                      # 1,294.00


# ---  정규표현식  ------------

import re

s = 'hi'

result1 = re.match(r'hi', s)
print(result1)               
# <re.Match object; span=(0, 2), match='hi'>
# span: 어디서부터 어디까지 매치했는지
# match : 무엇이 매치했는지

result2 = re.match(r'hey', s)
print(result2)
# None

# h 다음 아무 문자나 와도 된다는 패턴
result3 = re.match(r'h.', s)
print(result3)
# <re.Match object; span=(0, 2), match='hi'>

# * : 바로앞 글자가 0개 이상 와도 된다는 패턴
result4 = re.match(r'hi1*', s)
print(result4)
# <re.Match object; span=(0, 2), match='hi'>

# * : 바로앞 글자가 0개 이상 와도 된다는 패턴
result5 = re.match(r'hi1+', s)
print(result5)
# None

# ? : 바로앞 글자가 없을 수도 있다는 패턴
result6 = re.match(r'hi1?', s)
print(result6)
# <re.Match object; span=(0, 2), match='hi'>

s1, s2 = 'color', 'colour'
result7 = re.match(r'colou?r', s1)
print(result7)
# <re.Match object; span=(0, 5), match='color'>

result8 = re.match(r'colou?r', s1)
print(result8)
# <re.Match object; span=(0, 5), match='color'>

# \ : 특수 기호 무효화 → 해당 기호를 있는 그대로 사용할 수 있게 해줌
s3 = "how are you?"
result9 = re.match(r'how are you?', s3)
print(result9)
# <re.Match object; span=(0, 11), match='how are you'>

result10 = re.match(r'how are you\?', s3)
print(result10)
# <re.Match object; span=(0, 12), match='how are you?'>


# [] : 이 중 아무거나
s4 = "이 영화는 A등급 입니다."
pattern01 = r"이 영화는 [A-D]등급 입니다."
result11 = re.match(pattern01, s4)
print(result11)
# <re.Match object; span=(0, 14), match='이 영화는 A등급 입니다.'>

s5 = "이 영화는 F등급 입니다."
result12 = re.match(pattern01, s5)
print(result12)
# None

pattern02 = r"이 영화는 .등급 입니다."
result12 = re.match(pattern02, s5)
print(result12)
# <re.Match object; span=(0, 14), match='이 영화는 F등급 입니다.'>


# () : 캡쳐
s6 = "이 영화는 F등급 입니다."
print(s6.split('이 영화는 ')[1].split('등급')[0])
# F

pattern03 = r'이 영화는 (.)등급 입니다.'
result13 = re.match(pattern03, s6)
print(result13)
# <re.Match object; span=(0, 14), match='이 영화는 F등급 입니다.'>

result14 = re.findall(pattern03, s6)
print(result14)
# ['F']

pattern04 = r'이 (..)는 ([A-F])등급 입니다.'
result15 = re.findall(pattern04, s6)
print(result15)
# [('영화', 'F')]pattern04 = r'이 (..)는 ([A-F])등급 입니다.'
