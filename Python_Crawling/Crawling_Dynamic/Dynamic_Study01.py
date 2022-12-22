# 동적 크롤링 기초
'''
동적 웹사이트 특징
1. 사이트가 깜빡이지 않는다.
2. 화면이 한번에 다 로딩되지 않는다. (DOM 생성)
3. javascript가 필수이다.

서버 <-> 클라이언트의 흐름 및 특징
1. 데이터가 따로 따로 여러 군데에서 온다
2. 서버와 자주 통신한다.
3. 디자인이 화려하다.
4. 기능이 많고 사용성이 편리하다.

셀레니움 세팅하기!

필요한 것(크롬 기준!)
1. 크롬             파이어폭스, 사파리 등 다른 브라우저도 가능!
2. 크롬 driver      드라이버가 필요한 이유는 다양한 브라우저에 대응하기 위해 브라우저별 통신 규칙을 정해놓은 것
3. 셀레니움 파이썬 라이브러리   pip install selenium

+ 도커 설치 방법
1. docker
 - docker desktop 설치
 - docker hub에서 셀레늄 관련 컨테이너 주소 복사 selenium/standalone-chrome
 - cmd 창에 docker 명령어로 실행
   docker run -p 4444:4444 selenium/standalone-chrome
   -> -p : 포트의 약자
2. Python library

- 크롬은 자동 업데이트가 되므로 이에 맞는 크롬드라이버를 수시로 설치해줘야하는데 
  도커에서는 간단한 소스를 적용시켜 해당 부분은 자동화할 수 있다

* 도커 사용 시 주의사항
docker run -p 4444:4444 selenium/standalone-chrome
+ --shm-size="2g"    : 메모리 부족으로 에러 발생하는 것을 방지하기 위해 2G 할당
+ 크롬 옵션 추가 : --disable-dev-shm-usage, --no-sandbox
관련 에러
bind() failed cannot assign requested address (99)
Message: unknown error: session deleted because of page crash

* 도커 상태 확인
docker -ps -a
리스트 확인 후 돌아가고 있는 docker 정지
docker stop [컨테이너]

'''

# 테스트 코드 - 일반 설치
from selenium import webdriver
import time

browser = webdriver.Chrome("./Python_Crawling/Crawling_Dynamic/chromedriver.exe")
browser.get("http://naver.com")
time.sleep(5)
browser.close()

# 테스트 코드 - 도커
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# options.add_argument("--disable-dev-tools")
# options.add_argument("--no-zygote")
# options.add_argument("--single-process")
# options.add_argument("--whitelisted-ips")
# options.add_argument('user-agent= Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
browser = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)
# borwser = webdriver.Remote(command_executor='http://127.0.0.0:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
browser.get("http://naver.com")
print(browser.title)
browser.close()