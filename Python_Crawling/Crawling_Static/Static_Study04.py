# 쿼리스트링 활용
'''
쿼리스트링(query string)
- 웹 요청시에 보내는 추가 인자 값

쿼리스트링 형식
- ? 과 url로 구분된다 
  ex> url?querystring
- &로 값들이 구분된다
  ex> 값1=x&값2=y
- 배열
  ex> 배열명[값1,값2,값3...]   순서대로 파싱된다

url 인코딩
-> 문자를 인코딩하여 어디에서도 적용이 가능하도록 만들어줌
ex> 감자 = %EA%B0%90%EC%9E%90
'''

import requests as req

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B0%90%EC%9E%90"
res = req.get(url)
body = res.text
print(body)

# 한글로 쓰게 되더라도 알아서 인코딩된다!