# 자주 나는 오류 - stealth 셀레니움
'''
Selenium의 한계
- 웹서버들이 자동화된 봇을 막을 수 있음(접근 제한)

Stealth 라이브러리
- selenium이 티가 나지 않게 도와줌!

Tip! 셀레니움 사용 우뮤 판단 사이트
- https://intoli.com/blog/making-chrome-headless-undetectable/
'''

from selenium import webdriver
from selenium_stealth import stealth
import time

chrome = webdriver.Chrome("./Python_Crawling/Crawling_Dynamic/chromedriver.exe")

# 스텔스 적용
# https://pypi.org/project/selenium-stealth/
stealth(chrome,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

# 셀레니움 사용 유무 검사 사이트 (스텔스 미적용 시 faild)
url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
chrome.get(url)

time.sleep(10)

chrome.quit()
