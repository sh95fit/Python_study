import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 미사용
#from selenium import webdriver 
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

# 미사용
'''
def set_chrome_drier() :
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
'''

# 미사용
'''
driver = webdriver.Chrome(executable_path='C:/Users/tpgns/Desktop/Python_Study/Python_Basic/chromedriver.exe')
driver.implicitly_wait(10)  # 브라우저가 뜨고 나서 약 10초 정도 로딩될 때까지 기다린다
driver.get('https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword=bts')
webpage = driver.page_source
'''

f = open("./Python_Basic/crawling.txt", 'w', encoding='UTF-8')


c = open("./Python_Basic/crawling.csv", 'w', newline='')
writer = csv.writer(c)
csvtitle = ["제품명", "가격", "URL"]
writer.writerow(csvtitle)

webpage = urlopen('https://browse.gmarket.co.kr/search?keyword=%EC%9E%90%EB%8F%99%EC%B0%A8')
soup = BeautifulSoup(webpage, 'html.parser')

# 아래와 같이 했을 때 items의 내용이 잘려 제대로 list에 자식 클래스 서치가 되지 않음!
#items = soup.find('div', id='section__inner-content-body-container') 
#list = items.select("div:nth-child(4)")

# 대안
list = soup.select("#section__inner-content-body-container > div:nth-child(4)")
#print(list)

for item in list[0].find_all('div', class_="box__component") :
    title = item.find('span', class_="text__item")
    price = item.find('strong', class_="text__value")
    link = item.find('a', class_="link__item")['href']
    # link가 None 아니면 반영을 하는 방식도 있음!
#    if link != None :
#        link = item.find('a', class_="link__item")['href']
    if title != None and price != None and link != None :
        print(title.get_text(),price.get_text(), link)
        f.write("%s, %s, %s\n"%(title.getText(),price.getText(), link))
        data = []
        data.append(title.getText())
        data.append(price.getText())
        data.append(link)
        writer.writerow(data)

f.close()