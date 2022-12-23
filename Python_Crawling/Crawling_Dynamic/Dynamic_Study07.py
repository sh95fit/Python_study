# 자주 나는 오류 정리

# site loading 기다리기
'''
사이트 로딩 기다리기의 필요성
- 사이트에 원하는 데이터, 버튼이 존재하지 않을 수 있다.

기본적인 사이트 로딩 기다리기
selenium에서 기본적으로 기다려주는 항목
- HTTP Response 및 Rendering(javascript의 일부(event에 의해 실행되는 영역은 기다려주지 않음))을 기다림

- selenium에서 기본적으로 기다려주지 않는 항목에 대해 로딩을 기다리게 하는 명령어
 title_is   
 title_contains
 presence_of_element_located
 visibility_of_element_located
 visibility_of
 presence_of_all_elements_located
 text_to_be_present_in_element              // 비동기 데이터의 경우 데이터가 없더라도 element는 존재할 수 있다 / 이런 상황에서 사용!
 text_to_be_presnet-in_element_value        // text는 그 안에 값이 있는 경우 반환하므로 비동기 데이터 처리 시 보다 안전함!
 frame_to_be_available_and_switch_to_it     // 프레임이 생겼다 없어졌다 반복되는 경우 프레임이 존재하면서 사용이 가능할 때까지 기다렸다 사용 가능한 경우 연결
 invisibility_of_element_located
 element_to_be_clickable                    // 클릭이 가능해질 때까지 기다림 (ex> 동의 체크를 하지 않으면 버튼이 활성화되지 않음!)
 staleness_of
 element_to_be_selected
 element_located_to_be_selected
 element_selection_state_to_be
 element_located_selection_state_to_be
 alert_is_present                           // 경고창을 기다림
'''


# screenshot 찍기
#screenshot 찍기 + 파일 저장 및 css로 border 처리


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

url = ""

options = webdriver.ChromeOptions()
options.add_argument("window-size=1400,1000")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 전체 스크린샷을 위해 옵션 반영
# 실제로 창을 띄우지 않고 가상의 창을 메모리상에 띄움
options.add_argument("headless")

chrome =webdriver.Chrome("./Python_Crawling/Crawling_Dynamic/chromedriver.exe", options=options)

wait = WebDriverWait(chrome, 10)

def find_visible(css_selector) :
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

def finds_visible(css_selector) :
    find_visible(css_selector)
    return chrome.find_elements(By.CSS_SELECTOR, css_selector)


url = "https://naver.com"

chrome.get(url)


find_visible("input#query").send_keys("미국 증시\n")

# 해당 요소를 잘 가져오고 있는지 확인
e = find_visible("section[class='sc_new cs_stock'] div.dtcon_lst")
# 해당 요소를 잘 가져오고 있는지 확인
# print(e.text)

# 해당 요소만 스크린샷을 찍는 방법
e.screenshot("./Python_Crawling/Crawling_Dynamic/Dynamic_Part.png")

# 전체 스크린샷 찍는 방법
# 크롬의 창이 전체의 기준이 되므로 필요 요소를 담지 못할 수도 있다! (headless로 창을 띄우지 않는 방법으로 해결(옵션 추가!))
# chrome.set_window_size(1000,10000)  # 사이즈를 임의로 지정하게 되면 길이가 무한히 늘어나게 되므로 여백 공간이 발생

#chrome.save_screenshot("./Python_Crawling/Crawling_Dynamic/Dynamic_entire.png")


# 깔끔하게 존재하는 페이지 영역만 스크린샷을 찍는 방법
# body 태그 활용
# body 영역만 나오기는 하지만 윈도우 창 사이즈를 body 전체가 나올만큼 충분히 잡아주어야 한다!
chrome.set_window_size(1000,10000)
body = find_visible("body")
body.screenshot("./Python_Crawling/Crawling_Dynamic/Dynamic_entire.png")


# 특정 부분을 표시하는 방법!
# border 속성 활용   ex> border : 5px solid red;
# selenium은 attribute를 수정할 수 없으므로 javascript를 활용해야한다!
chrome.execute_script("""document.querySelector("section[class='sc_new cs_stock'] div.dtcon_lst").setAttribute('style', 'border : 5px solid red')""")
chrome.set_window_size(1000,10000)
body = find_visible("body")
body.screenshot("./Python_Crawling/Crawling_Dynamic/Dynamic_border.png")

chrome.quit()



