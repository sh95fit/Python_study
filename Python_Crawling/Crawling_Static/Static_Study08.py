# css 활용 실습
from bs4 import BeautifulSoup as BS
import requests as req
# module 'collections' has no attribute 'Callable' 에러 대응
# collections.Callable 참조가 파이썬 3.10부터 collections.abc.Callable로 이동하여, 제거된 Attribute라서 발생하는 오류
import collections     
if not hasattr(collections, 'Callable'):
    collections.Callable = collections.abc.Callable
#------------------------------------------------------------------

url = "https://search.shopping.naver.com/search/all?query=%EC%9A%B4%EB%8F%99%ED%99%94&cat_id=&frm=NVSHATC"
res = req.get(url)
soup = BS(res.text, "html.parser")

arr = soup.select("ul.list_basis div > a:nth-of-type(1)[title]")

for a in arr :
    print(a.get_text(strip=True))

# 무한 스크롤로 스크롤 될 때마다 불러오는 경우 일반적인 CSS Selector를 이용해 가져올 수 없다!
# 대안 : 동적 크롤링, 정규식 이용한 정적 크롤링

