# 판다스의 데이터 구조
'''
판다스의 데이터 구조
- 시리즈와 데이터프레임

1. 시리즈 
 - 동일 유형의 데이터를 저장하는 1차원 배열

2. 데이터프레임
 - 시리즈 데이터가 여러개 모여서 2차원적 구조를 갖는 것
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
series = pd.Series([1, 3, 5, 7, 9])

print(series)
'''

'''
# 이름 국어 영어 수학 총점 평균
name_series = pd.Series(["홍길동", "장보고", "이순신"])
kor_series = pd.Series([100,90,80])
eng_series = pd.Series([90,90,80])
math_series = pd.Series([100,100,80])
sum_series = pd.Series([290,280,240])
avg_series = pd.Series([96,93,80])

print(name_series, kor_series, eng_series, math_series, sum_series, avg_series)

# 데이터 프레임에 시리즈를 반영해 테이블 구성

df = pd.DataFrame({"이름" : name_series, "국어" : kor_series, "영어" : eng_series, "수학" : math_series, "총점" : sum_series, "평균" : avg_series})

print(df)
'''

'''
# ,로 구분되어 비어있는 경우 Unnamed로 표시된다 / 이를 없애려면 index_col = 0 옵션을 반영해준다 
df = pd.read_csv('./Python_Basic/countries.csv', index_col = 0)
print(df)
df = pd.read_csv('./Python_Basic/countries.csv')
print(df)

print(df['population']) # 원하는 데이터 열만 불러오고 싶은 경우

# 차트 표현
#df['population'].plot(kind='bar', color=('b','g','r','m','darkorange'))    # 막대 차트
df['population'].plot(kind='pie')   # 파이 차트
plt.show()
'''

'''
weather = pd.read_csv("./Python_Basic/weather.csv", encoding="CP949") # 한국말이 반영되어있을 경우 인코딩 에러가 발생할 수 있다!

print(weather.describe())   # count : 개수, mean : 평균, std : 표준편차, min, 25%, 50%, 75%, max
print(weather.count())  # 갯수만 구하고 싶은 경우
print(weather.mean())
print(weather['최대풍속'].mean())   # 특정 값의 평균만 보고 싶은 경우
print(weather[['최대풍속', '평균풍속']].mean())
print(weather['최대풍속'].sum())    # 최대풍속의 모든 데이터 합
'''

'''
# PyStudy_33.py의 판다스를 이용하지 않은 경우와 판다스를 이용한 경우 비교
weather = pd.read_csv("./Python_Basic/weather.csv", encoding="CP949")
monthly = [None for x in range(12)]
monthly_wind = [0 for x in range(12)]
weather['month'] = pd.DatetimeIndex(weather['일시']).month 

for i in range(12) :
    monthly[i] = weather[weather['month'] == i+1]
    monthly_wind[i] = monthly[i]["평균풍속"].mean()

plt.plot(monthly_wind, 'r')
plt.show()
'''

weather = pd.read_csv("./Python_Basic/weather.csv", encoding="CP949")
weather['month'] = pd.DatetimeIndex(weather['일시']).month 
means = weather.groupby('month').mean()

print(means)