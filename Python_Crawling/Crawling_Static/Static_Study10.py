# 자주 나오는 오류 정리
'''
정적 크롤링의 자주 나는 오류 대처방안
1. 브라우저 접속 시 되는데 requests로 되지 않는 경우!
  -> header 확인
2. 쿠키가 어디서 설정되는지 모르는 경우
  -> reauest를 확인하거나 브라우저 크롬 개발자 도구 활용
3. 매 요청 시 마다 값이 바뀌는 경우
  -> CSRF, 직접 파싱
4. 소스 보기 선택 시 값이 없는 경우
  -> XHR 연결 확인

1. 브라우저로 접속은 되지만 requests로 접속이 안 되는 경우
 - 브라우저도 결국 내부적으로는 HTTP 요청을 한다! 브라우저와 유사하게 요청을 보내면 해결 된다(헤더 포함 등)
 - 주요 헤더 반영
  : User-Agent, Cookie, Accept, Referer
 - 그 외 SPA, CSRF, Captcha, IP Ban 확인 필요

2. 쿠키(Cookie)
 - 쿠키의 유무는 로그인 여부에 따라 달라진다 (즉, 쿠키는 로그인 식별자와 같은 역할을 한다!)
 - 쿠키 유출 시 해킹 위험이 있다
 - 쿠키는 브라우저가 관리해준다!
 - Set-Cookie가 된 쿠키 정보를 가져와서 request에 반영해 활용한다
 - Name, Value, Domain, Path, Expires 등을 이용해 브라우저에서 관리
 - 쿠키를 브라우저에서 복사하는 방법
  : 크롬 개발자도구 -> Network -> 새로고침 -> Doc 선택 -> 쿠키 복사

3. CSRF (Cross-site Request Forgery)
 - 어떤 사이트를 함부로 실행시키는 것을 방지
  -> CSRF 토큰 or referer을 체크해 자동 실행 방지
    CSRF 토큰 : GET 요청으로 수시로 토큰을 받아와서 사용(요청 때마다 바뀜)
 - CSRF를 생성해주는 서버가 존재하기 때문에 해당 부분을 활용

4. 서버가 데이터를 즉각 주지 않는 상황
  - HTML 빈 껍데기만 주고 실제 내용물은 따로 패키징해서 주는 상태
   or 페이지가 바뀔 때 새로고침되지 않고 무한스크롤 되는 형태 등의 구조
  - XHR 확인 방법 
  크롬 개발자 도구 -> Network -> XHR 선택 후 원하는 페이지로 이동 or 새로고침 -> 원하는 데이터의 request URL 복사 후 크롤링

정적 크롤링의 한계
- Captcha
- Client-Side Javascript Dependency

-> requests는 브라우저를 흉내내기 힘들다
  따라서 브라우저를 사용해서 크롤링해야한다!
  => 셀레니움 활용(동적 크롤링)
'''

# requests로 헤더 없이 처리가 되지 않는 사이트 예시 - 쿠팡
import requests as req

res = req.get("https://coupang.com", headers={ 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})
print(res.text)
