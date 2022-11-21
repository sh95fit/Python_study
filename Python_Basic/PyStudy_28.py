#날씨 크롤링

#import datetime
from bs4 import BeautifulSoup  # 가져온 데이터를 html로 바꿔주는 모듈
from urllib.request import urlopen  #url 접속 및 데이터 가져오는 모듈

#서울 날씨
webpage = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8")
soup = BeautifulSoup(webpage, 'html.parser')

temp = ((soup.find('div', class_="_today")).find('div', class_="temperature_text").find("strong")).get_text() # tag(태크), attribute(id, class, 기타 등등 속성)을 이용해 찾기!
title = (soup.find('h2', class_="title")).get_text()

print(title)
print(temp)

#부산 날씨
webpage = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%B6%80%EC%82%B0%EB%82%A0%EC%94%A8")
soup = BeautifulSoup(webpage, 'html.parser')

temp = ((soup.find('div', class_="_today")).find('div', class_="temperature_text").find("strong")).get_text() # tag(태크), attribute(id, class, 기타 등등 속성)을 이용해 찾기!
title = (soup.find('h2', class_="title")).get_text()

print(title)
print(temp)

#제주 날씨
webpage = urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%A0%9C%EC%A3%BC%EB%82%A0%EC%94%A8")
soup = BeautifulSoup(webpage, 'html.parser')

temp = ((soup.find('div', class_="_today")).find('div', class_="temperature_text").find("strong")).get_text() # tag(태크), attribute(id, class, 기타 등등 속성)을 이용해 찾기!
title = (soup.find('h2', class_="title")).get_text()

print(title)
print(temp)