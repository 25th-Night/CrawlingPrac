# ---  문자열 메서드 : find, split  -------------


s = 'apple'

print(s.find('e'))

# array
arr = s.split('p')

print(arr)


# ------------------

s = '제 생일은 9월 입니다'

print(s.find('생'))
print(s.find('생일은'))


# ------------------

# 문자열 내에서 특정 문자열 다음 글자 가져오기

s = '제 생일은 9월 입니다'

# 공백을 포함한 문자열을 가져와 위치를 확인
pos = s.find('생일은 ')
# 문자열의 길이만큼 덧셈
pos += 4
# 해당 길이에 대한 문자열 추출
# 인덱싱이 아닌 슬라이싱으로 가져오기
print(s[pos:pos+1])


# ------------------

s = '제 생일은 10월 입니다'

arr = s.split('생일은 ')
s1 = arr[1]

arr2 = s1.split('월')
print(arr2)

bd = s.split('생일은 ')[1].split('월')[0]
print(bd)
