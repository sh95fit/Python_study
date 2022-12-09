# 크롤링 기초
'''
* 크롤링이란
 - 웹 크롤러
  : 조직적, 자동화된 방법으로 월드 와이드 웹(www)을 탐색하는 컴퓨터 프로그램
 - 검색을 원활하게 하기 위해 나옴

* 크롤링 활용처
 - 사이트에서 원하는 데이터 추출
 - 업무 자동화하기
 - 알림 받기

* 인터넷과 웹
 - 인터넷 : 네트워크 자체 (라우터들 간의 연결)
 - 웹 : 라우터들 사이 소통
 - 데이터는 압축되고 작을수록 전달에 유리하다(비용 절감, 빠른 속도, 높은 신뢰도)

* http와 소켓
 - HTTP : 웹 서버-클라이언트 간 통신할 때의 통신 규격
  : Request Line + 0개 이상의 헤더 + 빈 라인 + 바디

  1. Request Line
    ex> Method SP Request-URI SP HTTP-Version CRLF
        * SP : 공백 명령어(스페이스)
          CRLF : 줄바꿈 명령어 
  2. 0개 이상의 헤더
    ex> User-Agent : Mozilla/4.0 ...
        Host : www.xxxx.com
        Accept-Language : ko-kr     원하는 언어! (필수 조건은 아니다. 언어가 달라도 통신 가능)
        Accept-Encoding : gzip, deflate     암호화 시 사용
        Connection : Keep Alive     요청을 계속 새로 하지 않고 유지
        Content-Type : text/xml; charset=utf-8      주고 받을 데이터 타입      
        Content-Length : 1000       주고 받을 데이터 길이

  3. 빈 라인
    반드시 포함되어야 규격에 적합하게 통신이 가능하다!

 - HTTP Methods
  GET : 데이터를 주지 않고 받기만 하는 경우
  HEAD : 헤더만 가져올 때 사용
  POST : 데이터를 전달하고 받는 경우
  PUT : 수정(덮어씌우기)
  DELETE : 삭제
  OPTIONS

* HTTP - login
 
 상황 - 로그인 없이 데이터를 요청하는 경우
 요청 : GET /money HTTP/1.1
  -> 응답 : HTTP/1.1 401 Unauthorized   (미인증 시 발생되는 에러)

 * Tip! 응답의 분류
  100-199 : 정보전달용
  200-299 : 성공
  300-399 : 리다이렉트
  400-499 : 클라이언트 에러
  500-599 : 서버 에러

  -> 응답번호에 대한 의미를 확인하고 싶은 경우
     : http.cat/응답번호

 상황 - 로그인 진행
 요청 : POST /login HTTP/1.1
        User-Agent: Mozilla/4.0 (compatible; ...)     ====== 헤더 영역
                                                      ====== 빈 라인
        id=apple&password=banana                      ====== 바디 영역

  -> 응답 : HTTP/1.1 200 OK
            Set-Cookie : JSessionId=abcd1234

 상황 - 쿠키를 활용해 데이터 요청
 요청 : GET /money HTTP/1.1
       Cookie: JSessionId=abcd1234
  -> 응답 : HTTP/1.1 200 OK
           money=15000

* HTTP vs Socket
 - HTTP
  : request와 response가 무조건 짝을 이뤄 통신
 - Socket
  : request와 response가 자유롭게 쓰여지며 통신

* 브라우저
 - UI Rendering (HTML을 이미지화)
 - 특징
  1. 편의성
  2. 보안
  3. 스크립트 실행(동적 기능) - Javascript

* 웹앱과 API
 - 웹앱
  : 페이지 접속 시 골격만 로딩하고 내용은 API를 통해 요청하여 받아온다(API 기반 브라우저가 서버에 요청)
 - API : 상호 통신 규칙을 정의해놓은 것 - 재사용성이 큼!

* 크롤링 시 주의사항!(네티켓)
 - robots.txt : 크롤링 관련 규칙
  * : all 의미
  / : root를 의미 (모든 페이지 의미)
  아무 표시가 없으면 모든 페이지 크롤링 가능
'''

