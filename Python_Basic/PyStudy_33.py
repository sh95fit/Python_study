import csv

# 판다스(Pandas) 기초

'''
# weather.csv 파일 데이터 불러오기
f = open("./Python_Basic/weather.csv", "r")
data = csv.reader(f)
header = next(data)
for row in data :
    print(data)

f.close()
'''

'''
# 평균 풍속만 출력하기
f = open("./Python_Basic/weather.csv", "r")
data = csv.reader(f)
header = next(data)
for row in data :
    print(row[3], end=',')

f.close()
'''

'''
# 최대 평균 풍속 구하기
f = open("./Python_Basic/weather.csv", "r")
data = csv.reader(f)
header = next(data)
max_wind = 0

for row in data :
    if row[3] == '' :
        wind = 0
    else :
        wind = float(row[3])
    
    if max_wind < wind :
        max_wind = wind

print(f"최대 평균 풍속 : {max_wind}")

f.close()
'''

import matplotlib.pyplot as plt

# 최대 풍속이 속한 달 구하기
f = open("./Python_Basic/weather.csv", "r")
data = csv.reader(f)
header = next(data) # 타이틀 제외하기!
monthly_wind = [0 for x in range(12)]
days_count = [0 for x in range(12)]

max_wind = 0
max_month = 0

for row in data :
#    month = row[0].split('-')[1]
    month = int(row[0][5:7])
#    print(month)
    if row[3] != '' :
        wind = float(row[3])
        monthly_wind[month-1] += wind
        days_count[month-1] += 1

for i in range(12) :
    monthly_wind[i] /= days_count[i]
    if max_wind < monthly_wind[i] :
        max_wind = monthly_wind[i]
        max_month = i
#    print((i+1), monthly_wind[i])

print("최대 풍속 포함 월 ", (max_month+1))
plt.plot(monthly_wind)
plt.show()

f.close()