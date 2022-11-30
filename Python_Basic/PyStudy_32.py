import matplotlib.pyplot as plt
import numpy as np

years = [1965, 1975, 1985, 1995, 2005, 2015]
ko = [130,650,2500,12000,18000,27500]
jp = [890,5200,11500,42000,40500,38000]
ch = [100,200,290,550,1800,7900]

# 비교 차트 만들기 - matplotlib로는 만들 수 없으므로 numpy 사용!
'''
x_range = range(len(years))
plt.bar(x_range, ko, width=0.25)
plt.bar(x_range, jp, width=0.25)
plt.bar(x_range, ch, width=0.25)     #덮어 쓰여진다!
'''

# numpy 사용 - 비교 차트 만들기!
'''
x_range = np.arange(len(years))
plt.bar(x_range+0.0, ko, width=0.25)
plt.bar(x_range+0.25, jp, width=0.25)
plt.bar(x_range+0.5, ch, width=0.25)


plt.show()
'''

'''
# 산포도 차트
x = np.arange(20, 50)
y = x + 2*np.random.randn(30)

plt.scatter(x,y)    # 산포도 차트 => scatter

plt.show()
'''

# 파이 차트 만들기

times = [8, 14, 2]

t = ["SLEEP","STUDY","PLAY"]

plt.pie(times, labels=t, autopct="%.2f")  # autopct : 퍼센트를 몇 번째자리까지 표시할지를 지정

plt.show()