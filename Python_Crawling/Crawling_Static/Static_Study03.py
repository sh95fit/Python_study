# 정적 크롤링 - 환율 계산기

import requests as req

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)

# 크롤링 상태 확인
#print(res.text)
html = res.text

#split을 활용한 데이터 가져오기 - 미국 USD 환율
s = html.split('<span class="value">')[1].split('</span>')[0]
print(s)


# 정규식(Regular Expression)
'''
줄여서 regex, regexp

패턴 검색 기법(문자열에서 패턴을 분석해 추출)

ex> 정규식 활용 예
seriali[sz]e        # serialise or serialize
colou?r             # color or colour

기본 규칙
() : 캡처
[] : 대괄호 내 포함된 것 중 아무거나
. : 아무거나
* : 0개 이상
+ : 1개 이상
? : 포함되었거나 없거나
\ : 특수 기호 무효화

'''

import re

# 정규식 예제
s = 'hi'
print(re.match(r'hi1*', s))     # * : 별표 바로 앞글자가 0개 or 더 많이 존재
print(re.match(r'hi1+', s))     # + : + 앞글자가 1개 이상
print(re.match(r'hi1?', s))     # ? : 있거나 없을 수도 있는 경우

p = 'How are you?'
print(re.match(r'How are you\?', p))    # \ : 특수 기호 무효화

q = '이 영화는 D등급 입니다.'
print(re.match(r'이 영화는 [A-F]등급 입니다.', q))
print(re.match(r'이 영화는 [ABCF]등급 입니다.', q))

# split으로 등급 추출
print(q.split('영화는 ')[1].split('등급')[0])
# 패턴으로 등급 추출
print(re.findall(r'이 (..)는 (.)등급 입니다.', q)[0][1])


# 정규식을 이용한 환율 가져오기

url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.get(url)
body = res.text

# findall 활용

# 정규식을 미리 정의해둠으로써 준비에 사용되는 메모리를 줄이고 효율을 높임!
# Tip! .(dot)은 줄바꿈을 인식하지 못한다!  => re.DOTALL을 포함시켜 해당 문제를 해결
r = re.compile(r"h_lst.*?blind\">(.*?)</span>.*?value\">(.*?)</", re.DOTALL)     # .*? : 0개 이상 아무거나 가져오되 최소한으로 가져올 것
captures = r.findall(body)
print(captures)

print("----------------")
print("   환율 계산기   ")
print("----------------")
print("")

for c in captures :
    print(c[0] + " : " + c[1])

print()
usd = float(captures[0][1].replace(',', ''))
won = input("달러로 바꾸길 원하는 금액(원)을 입력하세요 : ")
won = int(won)
dollor = won / usd
dollor = int(dollor)
print(f"{dollor} 달러가 환전되었습니다.")