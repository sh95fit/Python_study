# Selenium 로그인 구현, 검색 및 출력, 무한스크롤, 탭 이동 (유저 인터렉션)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip    # 클립보드 - 복사(Copy) 시 임시로 저장되는 것이 가능하도록 해줌

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
login_button = find_visible(wait, "a#gnb_login_button")
print(login_button.text)
login_button.click()

time.sleep(3)

chrome.close()