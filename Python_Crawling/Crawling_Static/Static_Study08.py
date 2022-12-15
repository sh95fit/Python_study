# css 활용 실습
from bs4 import BeautifulSoup as BS
import requests as req
# module 'collections' has no attribute 'Callable' 에러 대응
# collections.Callable 참조가 파이썬 3.10부터 collections.abc.Callable로 이동하여, 제거된 Attribute라서 발생하는 오류
import collections     
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable
#------------------------------------------------------------------

# warning 경고창 안 뜨게 하기
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # InsecureRequestWarning 예외 처리

# 네이버 쇼핑 리스트 크롤링
# url = "https://search.shopping.naver.com/search/all?query=%EC%9A%B4%EB%8F%99%ED%99%94&cat_id=&frm=NVSHATC"
# res = req.get(url)
# soup = BS(res.text, "html.parser")

# arr = soup.select("ul.list_basis div > a:nth-of-type(1)[title]")

# for a in arr :
#     print(a.get_text(strip=True))

# 무한 스크롤로 스크롤 될 때마다 불러오는 경우 일반적인 CSS Selector를 이용해 가져올 수 없다!
# 대안 : 동적 크롤링, 정규식 이용한 정적 크롤링


# 쿠팡 - 광고 제외 리스트 크롤링
# 쿠팡은 일반 접근을 제한하므로 헤더를 활용해 user-agent 정보를 반영하면 해당 문제를 해결할 수 있다
url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
res = req.get(url, headers=hdr, verify=False)
soup = BS(res.text, "html.parser")


# 출력 확인
# arr = soup.select("div.name")
# for a in arr :
#     print(a.get_text(strip=True))

# 광고 제거하기
for desc in soup.select("div.descriptions-inner") :
    ads = desc.select("span.ad-badge")
    if len(ads) > 0 :
        print("광고!",end=' ')
#    elif len(ads) == 0 :
    print(desc.select("div.name")[0].get_text(strip=True))


# arr = [a.get_text(strip=True) for a in soup.select("div.name")]     : 위 내용을 한줄로 구성해 배열로 담음