# 동적 크롤링 - 페이지 이동
'''
크롬은 일반적으로 조종할 수 없도록 되어 있다!
크롬을 디버그 모드로 열어서 조종!
조종을 하기 위한 프로토콜이 있다(별도 언어로 구성되어 있음)
-> 크롬을 쉽게 접근할 수 있도록 만들어 놓은 것이 셀레니움이다
셀레니움이 다양한 환경에서 적용하도록 맞춰주는 것이 드라이버의 역할이다!

에러 해결
USB: usb_device_handle_win.cc:1045 Failed to read descriptor from node connection: 시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
-> 크롬 옵션을 추가하여 조치
options.add_experimental_option("excludeSwitches", ["enable-logging"])
'''


# 네이버 쇼핑 검색하기
from selenium import webdriver
import time     # sleep 활용

# 크롬 옵션 적용 (add_argument : 인자를 추가할 때 활용 / add_encoded_extension : 확장 프로그램을 확인하고 싶은 경우 활용)
options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")   # window-size=가로,세로
options.add_argument("no-sandbox")  # 샌드박스 미활용 (샌드박스 - 보안상 영역을 구분하여 조종 영역을 분리하는 역할) - 즉, 보안상 영역을 구분하지 않고 여러 영역(탭)을 조종하기 위해 꺼줌
# options.add_argument("headless")    # 크롬창을 안 보이도록 설정
options.add_experimental_option("excludeSwitches", ["enable-logging"])      # 연결된 장치들을 서치해 발생하는 에러를 표시하지 않기 위해 추가

# 셀레니움이 크롬드라이버를 연결하는 것
chrome = webdriver.Chrome("./Python_Crawling/Crawling_Dynamic/chromedriver.exe", options=options)

# 크롬 페이지 이동
chrome.get("https://naver.com")     # requests의 get과는 다름! (이동을 의미)
chrome.get("https://shopping.naver.com")
chrome.back()
chrome.forward()

# 세션이 적용된 것을 확인하기 위해 코드 실행을 일시적으로 멈춤
time.sleep(3)

# 브라우저 종료
chrome.close()