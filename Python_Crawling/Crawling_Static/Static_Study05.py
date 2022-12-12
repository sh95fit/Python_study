# Beautifulsoup 모듈 활용
'''
beautifulsoup
- html 통신을 편하게 해줌
- 주요 기능
 html 문자열 파싱
 html 노드 인식 및 편리한 기능 활용 가능
 parent, children, contents, descendants, sibling
 string, strings, stripped_strings, get_text()
 prettify       - 소스를 보기 편하게 만듦어줌
 html attribute

차이점
--------------------------
requests
- http 통신을 편하게 해줌
--------------------------
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
for td in tds:
    if len(td.find_all("a")) == 0 :
        continue
    names.append(td.get_text(strip=True))  # strip=True : 공백 제거
    # for s in td.strings :
    #     print(s)
    # for s in td.stripped_strings:
    #     print(s)

prices = []
for td in tds :
    if "class" in td.attrs :
        if "sale" in td.attrs["class"] :
            prices.append(td.get_text(strip=True))


print(names)
print(prices)