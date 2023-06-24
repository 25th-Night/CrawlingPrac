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
