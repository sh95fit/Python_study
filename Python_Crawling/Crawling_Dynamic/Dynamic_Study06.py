# 동적 크롤링 프로젝트 - 다나와 PC 견적
# iframe, 카테고리 클릭

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os

# 태그 내 속성의 값을 가져오기 위한 bs4 활용
import requests
from bs4 import BeautifulStoneSoup



# 다나와 PC 견적 사이트
url = "https://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1400,1000")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

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

# iframe으로 프레임별로 다른 HTML을 활용하는 영역으로 이동하기 위한 함수
def Frame(id) :
    chrome.switch_to.parent_frame()     # 부모 프레임으로 이동 (기본 프레임)
    find_visible("iframe#"+id)
    chrome.switch_to.frame(id) 

# 제조사 옵션 출력 함수
def choose_one(text, options) :
    print("-------------------------")
    print(text)
    print("-------------------------")
    for i in range(len(options)) :
        print(f"{i+1}. {options[i].get_attribute('data')}")
    choose = input(">>> ")
    return int(choose) 

# 제조사 이외 옵션 출력 함수
def choose_one_op(text, options):
    print("-------------------------")
    print(text)
    print("-------------------------")
    for i in range(len(options)):
        print(f"{i+1}. {options[i].text}")
    choose = input(">>> ")
    return int(choose)

# 공통되는 CSS SELECTOR 경로를 함수로 지정해서 다른 장비에서도 가져다 씀!
def parse_products() :
    products = []
    for p in finds_visible("table.tbl_list > tbody > tr[class^=productList_]") :
        name = p.find_element(
            By.CSS_SELECTOR, "td[class=title_price] p[class=subject]").text
        try:
            price = p.find_element(
                By.CSS_SELECTOR, "td[class=rig_line] span[class=prod_price]").text
        except:
            continue
        # print(name + "   " + price)
        products.append((name, price))
    return products

# 제조사 선택을 위한 함수
def choose_maker(text) :
    # 옵션 전체 보기 선택
    find_visible("div.search_option_title button").click()

    # 제조사 선택
    makers = finds_visible("input[name=makerCode]")

    # for i in range(len(cpu_makers)) :
    #     print(str(i+1) + ". " + cpu_makers[i].get_attribute('data'))    # get_attribute : 태그 내 속성의 값을 가져올 때 사용
    num = choose_one(text + " 제조사", makers)
    print(makers[num-1].get_attribute('data'))
    # 클릭 요소가 span 태그로 되어 있어 따로 아래와 같이 span 태그+ nth-child 조합으로 활용한다
    select = find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(1) > div.search_cate_contents > ul > li:nth-child({num}) > label > span")
    select.click()

    return num



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
category = {
    "CPU" : "873",
    "메인보드" : "875",
    "메모리" : "874",
    "그래픽카드" : "876",
    "SSD" : "32617",
    "케이스" : "879",
    "파워" : "880",
}

category_css = {
    # Dictionary Comprehension
    c: "dd.category_" + category[c] + " a" for c in category
    # 반복이 필요
    # "CPU": "dd.category_" + catagory["CPU"] + " a",
    # "메인보드": "dd.category_" + catagory["메인보드"] + " a",
    # "메모리": "dd.category_" + catagory["메모리"] + " a",
    # "그래픽카드": "dd.category_" + catagory["그래픽카드"] + " a",
    # "SSD": "dd.category_" + catagory["SSD"] + " a",
    # "케이스": "dd.category_" + catagory["케이스"] + " a",
    # "파워": "dd.category_" + catagory["파워"] + " a",
}

# iframe이 있는 경우 카테고리 지정 페이지 이동
def go_to_category(category_name) :
    # Frame(id)
    find_visible(category_css[category_name]).click()
    time.sleep(1)

# CPU 카테고리 클릭
# cpu = find_visible(category_css["CPU"])
# cpu.click()
go_to_category("CPU")

time.sleep(1)

# CPU 조건 선택

# # 옵션 전체 보기 선택
# find_visible("div.search_option_title button").click()

# # CPU 제조사 선택
# cpu_makers = finds_visible("input[name=makerCode]")

# # for i in range(len(cpu_makers)) :
# #     print(str(i+1) + ". " + cpu_makers[i].get_attribute('data'))    # get_attribute : 태그 내 속성의 값을 가져올 때 사용
# num = choose_one("CPU 제조사", cpu_makers)
# print(cpu_makers[num-1].get_attribute('data'))
# # 클릭 요소가 span 태그로 되어 있어 따로 아래와 같이 span 태그+ nth-child 조합으로 활용한다 
# select = find_visible(
#     f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(1) > div.search_cate_contents > ul > li:nth-child({num}) > label > span")
# select.click()

# 함수로 전환
cpu_idx = choose_maker("CPU")


# CPU 종류 선택
is_intel = False
is_amd = False
if (cpu_idx-1) == 0 :
    is_intel = True
    find_visible(
        "#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents > button").click()  # 제조사 호환 CPU 선택
    options = finds_visible(    
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents.open > ul > li")   # 해당 CPU 리스트 불러오기
    i = choose_one_op("인텔 CPU 종류 선택", options)
    find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"
    ).click()

elif (cpu_idx-1) == 1 :
    is_amd = True
    find_visible(
        "#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents > button").click()
    options = finds_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li")
    i = choose_one_op("AMD CPU 종류 선택", options)
    find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"
    ).click()

time.sleep(2)

# CPU 제품 목록 가져오기

# CSS SELECTOR - OR 연산 = 쉼표(,) But 상품명과 금액 매칭이 어려움!
# list = finds_visible(
#     "table.tbl_list > tbody > tr[class^=productList_] td[class=title_price] p[class=subject], table.tbl_list > tbody > tr[class^=productList_] td[class=rig_line] span[class=prod_price]")

# 따로 가져오는 방법
# name = finds_visible("table.tbl_list > tbody > tr[class^=productList_] td[class=title_price] p[class=subject]")
# price = finds_visible("table.tbl_list > tbody > tr[class^=productList_] td[class=rig_line] p")

# 공통 노드에서 분기 시켜서 가져오는 방법
# 판매중지 항목을 포함하고 싶은 경우!
# products = finds_visible("table.tbl_list > tbody > tr[class^=productList_]")
# for i in products :
#     name = i.find_element(By.CSS_SELECTOR, "td[class=title_price] p[class=subject]").text
#     price = i.find_element(By.CSS_SELECTOR, "td[class=rig_line] p").text    # 판매중지 때문에 span 태그 활용이 어려워 p 태그 이용
#     print(name + "   " + price)
# 판매중지 항목 미포함
# products = finds_visible("table.tbl_list > tbody > tr[class^=productList_]")
# cpu_list = []   # 항목을 가져와 별도로 담을 리스트
# for i in products :
#     name = i.find_element(By.CSS_SELECTOR, "td[class=title_price] p[class=subject]").text
#     try :
#         price = i.find_element(By.CSS_SELECTOR, "td[class=rig_line] span[class=prod_price]").text
#     except :
#         continue
#     # print(name + "   " + price)
#     cpu_list.append((name,price))

# 위 판매중지 항목 미포함을 함수로 구현하여 가져오기
cpu_list = parse_products()

for cpu in cpu_list :
    print(cpu)




# 메인보드 선택하기
go_to_category("메인보드")


# 메인보드 제조사 선택
mainboard_idx = choose_maker("메인보드")

# 선택한 CPU를 통해 자동적으로 호환되는 제품 종류 선택
if is_intel == True :
    find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents > ul > li:nth-child(1) > label > span"
    ).click()
elif is_amd == True :
    find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents > ul > li:nth-child(2) > label > span"
    ).click()
else :
    find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents > ul > li:nth-child(3) > label > span"
    ).click()

time.sleep(2)

mainboard_list = parse_products()

for mainboard in mainboard_list:
    print(mainboard)




# 메모리 선택하기
go_to_category("메모리")

# 메모리 제조사 선택
choose_maker("메모리")

# 사용 장치 선택(데스크탑 고정)
find_visible("#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents > ul > li:nth-child(1) > label > span").click()

# 제품 분류 선택
options = finds_visible(
    f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents > ul > li")
    # f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li")
i = choose_one_op("메모리 제품 분류", options)
find_visible(
    f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents > ul > li:nth-child({i}) > label > span"
    # f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"    # 전체 보기 버튼 추가시 활용
).click()

# 용량 선택
options = finds_visible(
    f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(4) > div.search_cate_contents > ul > li")
    # f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li")
i = choose_one_op("메모리 용량 선택", options)
find_visible(
    f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(4) > div.search_cate_contents > ul > li:nth-child({i}) > label > span"
    # f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"    # 전체 보기 버튼 추가시 활용
).click()

time.sleep(2)

memory_list = parse_products()

for memory in memory_list:
    print(memory)




# 그래픽카드 선택
go_to_category("그래픽카드")
is_NVIDIA = False
is_AMD = False

# 그래픽카드 제조사 선택
choose_maker("그래픽카드")

# 칩셋 제조사 선택
options = finds_visible(
    f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents > ul > li")
# f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li")
i = choose_one_op("칩셋 제조사 선택", options)
if i == 1:
    is_NVIDIA = True
elif i == 2 :
    is_AMD = True
find_visible(
    f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(2) > div.search_cate_contents > ul > li:nth-child({i}) > label > span"
    # f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"    # 전체 보기 버튼 추가시 활용
).click()


# # 제품 시리즈 선택
# options = finds_visible(
#     f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents > ul > li")
# # f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li")
# i = choose_one_op("제품 시리즈 선택", options)
# find_visible(
#     f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents > ul > li:nth-child({i}) > label > span"
#     # f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(3) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"    # 전체 보기 버튼 추가시 활용
# ).click()

# 칩셋 선택
if is_NVIDIA : 
    find_visible("#estimateMainSearchOption > div > div.search_option_list > div:nth-child(5) > div.search_cate_contents > button").click()
    options = finds_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(5) > div.search_cate_contents.open > ul > li")
    i = choose_one_op("NVIDIA 칩셋 선택", options)
    find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(5) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"
    ).click()
elif is_AMD:
    find_visible("#estimateMainSearchOption > div > div.search_option_list > div:nth-child(6) > div.search_cate_contents > button").click()
    options = finds_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(6) > div.search_cate_contents.open > ul > li")
    i = choose_one_op("AMD 칩셋 선택", options)
    find_visible(
        f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(6) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"
    ).click()

time.sleep(3)

graphic_list = parse_products()

for graphic in graphic_list:
    print(graphic)


# SSD
go_to_category("SSD")

choose_maker("SSD")

# 용량 선택
options = finds_visible("#estimateMainSearchOption > div > div.search_option_list > div:nth-child(5) > div.search_cate_contents > ul > li")
i = choose_one_op("SSD 용량 선택", options)
find_visible("#estimateMainSearchOption > div > div.search_option_list > div:nth-child(5) > div.search_cate_contents > button").click()
find_visible(
    f"#estimateMainSearchOption > div > div.search_option_list > div:nth-child(5) > div.search_cate_contents.open > ul > li:nth-child({i}) > label > span"
).click()

time.sleep(2)

memory_list = parse_products()

for memory in memory_list:
    print(memory)

time.sleep(5)


chrome.quit()