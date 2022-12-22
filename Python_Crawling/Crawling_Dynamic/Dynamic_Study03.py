# 동적 크롤링 - 페이지 로딩, Element 찾기
'''
문서를 모두 로딩한 다음에 javascript 실행
-> 목표가 되는 데이터를 얻기 위해서는 javascript가 다 실행될 때까지 기다려줘야 한다!
-> OnLoad -> 이벤트 체이닝

selenium get 자체가 웹페이지의 로딩을 기다려줌
but 추가적인 데이터(javascript 실행으로 나타나는 데이터)가 로딩될 때까지 기다려주지 않는다!

-> 전체 로딩이 완료되어야 필요한 데이터의 추출이 올바르게 이루어진다
* 로딩 - 웹서버가 HTML 응답을 주면 HTML을 그리고 css, js를 적용하는데 걸리는 시간

'''

from selenium import webdriver
import time

# 로딩 관련 클래스 import 설정
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("window-size=1000,1000")
options.add_argument("no-sandbox")
options.add_argument("--disable-gpu")

chrome = webdriver.Chrome("./Python_Crawling/Crawling_Dynamic/chromedriver.exe", options=options)

chrome.get("https://shopping.naver.com")

# javascript 실행하여 완전한 로딩이 될 때까지 기다린다 (로딩 시간이 설정 시간보다 긴 경우 대응이 불가능 하다!)
# time.sleep(3)     # 파이썬의 기능
#chrome.implicitly_wait(3)   # 셀레늄이 제공하는 기능

# #원하는 Element를 기준으로 로딩을 판단하여 처리(ex> 네이버 입력창)
wait = WebDriverWait(chrome, 10)    # 부가 조건 등으로 해당 요소가 로딩될 때까지만 기다리며 10초는 로딩의 마지노선
# 해당 요소가 로딩될 때까지 기다림과 동시에 해당 요소를 가져옴!
el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "form[name=search] div > input")))


# 위 내용을 반복적으로 사용하기 위해 함수로 설정
def find(wait, css_selector):
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

search = find(wait, "form[name=search] div > input")
search.send_keys("갤럭시 버즈2\n")      # \n : 새로운 줄을 만들기 위해 셀레늄은 엔터를 입력하는 행위를 실행!

# 검색 버튼을 클릭하여 페이지 이동
# button = find(wait, "button._searchInput_button_search_1n1aw")
# button.click()

time.sleep(3)

# id, name, class_name, css_selector, xpath, link_text, tag_name 등을 활용해 element를 찾음!
# time.sleep(3)     # 로딩이 되길 기다림! (충분한 시간을 주지 않을 경우 제대로 로딩이 되지 않아 찾지 못할 수 있음!)
#el = chrome.find_element(By.CSS_SELECTOR, 'form[name=search] div > input')
print(el)
chrome.close()