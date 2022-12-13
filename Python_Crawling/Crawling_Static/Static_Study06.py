# css selector 활용 크롤링
'''
# css란?
Cascading Style Sheets
html로 잡힌 골격에 스타일링(색, 크기 등)을 하는 것
스타일의 이름으로 구조가 특정지어질 수 있음(css selector)

CSS selector
- 웹 구성 시 CSS Selector을 직접 활용해 이름을 붙혀 만들기 때문에 CSS Selector로 찾아질 가능성이 높다

- Element Type 방식
 태그 값들이 selector의 기준이 된다
- ID 방식
 태그 내 id 값이 존재하면 id값이 selector의 기준이 된다
- Class 방식
 태그 내 class 값이 존재하는 경우 class값이 selector의 기준이 된다
- 고급 한정자 방식
 id, class가 없는 경우 기준이 되는 것
 ex> nth-child  


'''

from bs4 import BeautifulSoup as BS     #HTML을 편하게 다룰 수 있게 해줌
import requests as req      # HTTP 통신을 위해 사용

# module 'collections' has no attribute 'Callable' 에러 대응
# collections.Callable 참조가 파이썬 3.10부터 collections.abc.Callable로 이동하여, 제거된 Attribute라서 발생하는 오류
import collections     
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable
#------------------------------------------------------------------

url = "https://finance.naver.com/marketindex/exchangeList.naver"
res = req.get(url)
#print(res.text)
soup = BS(res.text, "html.parser")

# 출력 테스트
# print(soup.title)
# print(soup.title.string)

# 원하는 영역 찾기
tds = soup.find_all("td")

names = []
for td in soup.select("td.tit") :
    names.append(td.get_text(strip=True))

prices = []
for td in soup.select("td.sale") :
    prices.append(td.get_text(strip=True))


print(names)
print(prices)