# 동적 크롤링 프로젝트 - 다나와 PC 견적
# iframe, 카테고리 클릭

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

# 다나와 PC 견적 사이트
url = "https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1400,1000")

chrome =webdriver.Chrome("./Python_Crawling/Crawling_Dynamic/chromedriver.exe", options=options)


# 요소가 로딩될 때까지 기다렸다 해당 요소를 가져오는 함수
# presence : 존재 유무 판단, visibility : 화면에 보이는 요소 판단
wait = WebDriverWait(chrome, 10)

def find_present(css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))  # 내부를 튜플로 받아야 한다!

def finds_present(css_selector) :
    find_present(css_selector)
    return chrome.find_elements(By.CSS_SELECTOR, css_selector)

def find_visible(css_selector):
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_visible(css_selector):
    find_visible(css_selector)
    return chrome.find_elements(By.CSS_SELECTOR, css_selector)

# 다나와 PC 견적 웹페이지 접속
chrome.get(url)

# 다나와 PC 견적 웹사이트는 iframe을 활용해 프레임 내 별도 HTML 페이지로 구성되어 있는 경우가 있음
# 해당 프레임(iframe)의 페이지로 이동이 필요한 경우
# find_visible("iframe#[iframe 아이디]")    # 로딩이 될 때까지 기다림!
# chrome.switch_to.frame("[iframe 아이디]")

# PC 주요부품 항목 불러오기 확인
# list = finds_present("dl[class=pd_list] dd")

# for i in list :
#     print(i.text)

# 항목을 리스트 번호로 선택하는 방법
# finds_visible("dl[class=pd_list] dd")[1].click()
# time.sleep(3)


# 클래스의 카테고리 영역의 번호를 지정해둔 후 이를 불러와 활용하는 방법
catagory = {
    "CPU" : "873",
    "메인보드" : "875",
    "메모리" : "874",
    "그래픽카드" : "876",
    "SSD" : "32617",
    "케이스" : "879",
    "파워" : "880",
}


cpu = find_visible("dd.category_" + catagory["CPU"] + " a")
cpu.click()

mainboard = find_visible("dd.category_" + catagory["메인보드"] + " a")
mainboard.click()

time.sleep(5)


chrome.quit()

