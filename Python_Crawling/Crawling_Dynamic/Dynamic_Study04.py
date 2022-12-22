# Selenium 로그인 구현, 검색 및 출력, 무한스크롤, 탭 이동 (유저 인터렉션)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip    # 클립보드 - 복사(Copy) 시 임시로 저장되는 것이 가능하도록 해줌
from Dynamic_info import id_info, pw_info

chrome = webdriver.Chrome("./Python_Crawling/Crawling_Dynamic/chromedriver.exe")
wait = WebDriverWait(chrome, 10)
short_wait = WebDriverWait(chrome, 3)

def find(wait, css_selector) :
    return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))) 

def find_visible(wait, css_selector) :
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

chrome.get("https://shopping.naver.com")


# 로그인 버튼을 찾아서 클릭 
# 주의사항 : 로그인 버튼이 나타났다고 해서 기능까지 사용이 가능한 상태가 되지 않았을 경우가 있을 수 있음!
# -> 대안 EC.presence_of_element_located 대신 visibility_of_element_located 사용!
# login_button = find_visible(wait, "a#gnb_login_button")
# print(login_button.text)
# login_button.click()
find_visible(wait, "a#gnb_login_button").click()        # 로그인 이동 간단 코드

# 로그인하기
# send_keys를 통한 직접 입력으로 로그인 시도 시 캡차 때문에 로그인이 정상적으로 이루어지지 않는다!
# pyperclip을 이용해 로그인!
input_id = find_visible(wait, "input#id")
#input_id.send_keys(id_info)
pyperclip.copy(id_info)
input_id.send_keys(Keys.CONTROL, "v")

input_pw = find_visible(wait, "input#pw")
#input_pw.send_keys(pw_info+"\n")
# input_pw.send_keys(pw_info)
pyperclip.copy(pw_info)
input_pw.send_keys(Keys.CONTROL, "v")
input_pw.send_keys("\n")

# 로그인 후 로딩되는 동안 기다려줌 (로그아웃 버튼은 보이지 않으므로 존재 여부로 판단)
find(wait, "a#gnb_logout_button")

# 버튼 클릭을 생략할 경우 비밀번호 뒤에 \n 추가
# login_button = find_visible(wait, "div.btn_login_wrap > button")
# login_button.click()


# 로그아웃 기능 구현
# myinfo = find_visible(wait, "a.gnb_my")
# myinfo.click()

# logout = find_visible(wait, "a#gnb_logout_button")
# logout.click()

# OTP 인증을 위한 시간
#time.sleep(5)

# 검색
search = find_visible(wait, "form[name=search] input")
search.send_keys("아이폰 케이스")
# 한글 입력 후 바로 \n 시 적용이 되지 않을 수 있으므로 분리
time.sleep(1)
search.send_keys("\n")

# 태그 정리
'''
ex>
a.logout_button
a[class="logout_button"]
a[class^="logout"]  # logout으로 시작되는 a 태그를 모두 가져온다
a[class$="button"]  # button으로 끝나는 a 태그를 모두 가져온다
a[class*="out_but"] # 해당 글자가 포함된 a 태그를 모두 가져온다
'''

find_visible(wait, "a[class^=basicList_link__]")     # a 태그를 하나만 불러올 수 있다! wait를 통해 로딩이 되길 기다리는 용도로 활용


# 무한 스크롤 로딩 방법(script 활용!(Javascript))
# chrome.execute_script("window.scrollBy(0, 10000)")  # 스크롤을 한번 내려서 끝나지 않고 여러번 내려야 모든 상품을 확인할 수 있다
# chrome.execute_script("window.scrollBy(0, document.body.scrollHeight)")     # document 바디 부분이 스크롤로 내릴 수 있는 최대 길이를 반환해준다  But, 최초 로딩 시 바디는 짧으므로 상품 검색이 불가능함!
# 즉 문서의 바디 부분은 스크롤을 일정치 이상 내렸을 때 조금씩 늘어나는 형태로 구현되어 있음!
# 스크롤을 여러번 실행한 후 상품 검색
for i in range(10) :
    chrome.execute_script("window.scrollBy(0, " + str((i+1)*2000) + ")")    # 스크롤 범위를 조금씩 늘림
# 로딩에 시간이 소요되므로 sleep 추가
time.sleep(1)



# 상품 목록 가져오기
# 로딩이 끝나면 a 태그 전체 요소를 불러옴 - 크롬에서 지원
# lists = chrome.find_elements(By.CSS_SELECTOR, "a[class^=basicList_link__]")       # 일부 다른 파트에서도 해당 클래스명칭을 사용해 섞여서 출력됨
# lists = chrome.find_elements(By.CSS_SELECTOR, "div[class^=basicList_title__]")    # 항목 이름만 가져올 경우 활용 가능! (광고 제거가 까다로움)
# Selenium에서는 형제 노드를 찾는 것보다 공통 부모 노드를 찾는 것이 유리하다!
lists = chrome.find_elements(By.CSS_SELECTOR, "div[class^=basicList_info_area__]")  # 광고와 분리하기 위해 제목, 광고의 부모 노드를 lists로 담아 분류

for list in lists :
    # 광고 필터링 하기
    try :
        list.find_element(By.CSS_SELECTOR, "button[class^=ad_ad_stk__]")
        continue
    except :
        pass
    print(list.find_element(By.CSS_SELECTOR, "div[class^=basicList_title__]").text)


#time.sleep(5)

chrome.close()