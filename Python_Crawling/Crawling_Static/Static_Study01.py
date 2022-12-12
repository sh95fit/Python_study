# 정적크롤링 vs 동적 크롤링
'''
-       정적 크롤링               vs             동적 크롤링
       빠르고 간단함                            느리고 복잡함
 처음엔 쉽지만 고도화가 힘듦            처음엔 손이 많이 가지만 나중에 편리
       테스트가 쉬움                           테스트가 어려움
   상대적으로 오류가 적음                   상대적으로 오류가 높음

- 크롬 개발자 도구
 F12 or 도구 더보기 -> 개발자 도구
 탭 종류
 - Elements
  웹페이지의 실제 소스코드를 보여줌(HTML 구조 파악이 가능)
  * HTML이란? HyperText Markup Language로 구조를 잡아주는 언어를 뜻함
  원하는 데이터 위치 파악 시 활용
  웹의 원소, 최소 단위를 분석

 - Console
  동작을 담당하는 JavaScript를 실행해보는 탭
  디버깅할 때 매우 유용

 - Sources
  여러가지 불러온 파일을 보여주는 탭

 - Network
  웹에서 주고 받는 모든 네트워크 통신을 확인할 수 있는 탭
 - Performance
  웹페이지 성능 파악 시 활용하는 탭

 - Application
  고도화 시 쿠키에 관련된 부분을 처리할 때 활용할 수 있는 탭
  웹페이지와 관련된 저장소 영역을 보여줌

- request 라이브러리
  주요 함수
  get() : 요청, 값을 가져오는 역할
  post() : 생성, 액션
  put() : 수정, 덮어씌우기
  delete() : 삭제

  text
  json()

'''

# request 사용 형태
import requests as req

url = "http://www.naver.com/"
#res = req.get(url)
#print(res.text)

# GET 접속해보기 - 자신 아이피 알아보기
url = "https://api.ipify.org/"
res = req.get(url, headers={'Player' : 'KIMSEHUN'})
print(res.status_code)
print(res.text)
print(res.request.method)
print(res.request.headers)
print(res.elapsed)
print(res.raw)  # 바이트값을 그대로 받아 사용할 때 활용(이미지 크롤링 시!)