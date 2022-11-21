import datetime
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

now = datetime.datetime.now()
nowDate = now.strftime("%Y%m%d%H%M")
filename = "%s.txt"%(nowDate)
csvname = "%s.csv"%(nowDate)
f = open("./Python_Basic/"+filename, 'w', encoding='UTF-8')
csvfile = open("./Python_Basic/"+csvname, 'w', newline="")  #엑셀로 저장 시 엔코딩하면 읽을 수 없음!(encoding="UTF-8 미적용)
writer = csv.writer(csvfile)
title = ["순위","웹툰명"]
writer.writerow(title)

# 네이버 웹툰 실시간 인기급상승 크롤링
webpage = urlopen("https://comic.naver.com/index")
soup = BeautifulSoup(webpage, 'html.parser')

ranks = soup.find('ol', id="realTimeRankFavorite")

i = 1
#find_all(tag, attribute), findAll(tag) - 목록 형태로 가져올 때 사용 (하나만 가져오는 경우 find 사용!)
for rank in ranks.find_all('li') : 
    text = rank.find('a')
    print("%d위 %s"%(i,text.get_text()))

    # 텍스트 파일 출력 방식
    f.write("%d위 %s\n"%(i,text.get_text()))
    
    #csv 출력 방식
    data = []
    data.append(i)
    data.append(text.get_text())
    writer.writerow(data)
    
    i += 1
f.close

print("----------------다른 풀이-----------------")

for i in range(1,11) :
    if(i<10) :
        ranking = (((soup.find('ol', id="realTimeRankFavorite")).find('li', class_="rank0"+str(i))).get_text()).split()
        print(ranking[0])
    else :
        ranking = (((soup.find('ol', id="realTimeRankFavorite")).find('li', class_="rank"+str(i))).get_text()).split()   
        print(ranking[0])