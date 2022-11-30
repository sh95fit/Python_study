import matplotlib.pyplot as plt
'''
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.0, 22105.3]

plt.plot(years, gdp, color='blue', marker = 'o', linestyle='dotted')
plt.title("GDP FOR YEAR")
plt.ylabel("Dollars")
plt.xlabel("Years")
plt.savefig("./Python_Basic/test.png", dpi = 600)
plt.show()
'''

'''
# x축과 y축 바꿔보기
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.0, 22105.3]

plt.plot(gdp, years, color='blue', marker = 'o', linestyle='dotted')    # r : red, g : green, b : brue ... 풀네임도 가능하지만 1글자로도 반영가능!
plt.title("GDP FOR YEAR")
plt.ylabel("Years")
plt.xlabel("Dollars")
plt.savefig("./Python_Basic/test.png", dpi = 600)
plt.show()
'''

'''
x = [x for x in range(-10, 10)]
y = [2*t for t in x]
plt.plot(x,y,marker='o')

plt.axis([-20, 20, -20, 20])    # x축, y축 축의 범위를 지정해주고 싶을 때 사용
plt.show()
'''

'''
x = [x for x in range(20)]
y = [x**2 for x in range(20)]
z = [x**3 for x in range(20)]

plt.plot(x, x, label='linear', marker='o')
plt.plot(x, y, label='quardratic', marker='x')
plt.plot(x, z, label='cubic', marker='v')

plt.legend()    # 범례를 표시하고 싶을 때 사용
plt.show()
'''

'''
import math

x = []
y = []

for angle in range(360) :
    x.append(angle)
    y.append(math.sin(math.radians(angle)))

plt.plot(x, y, label='sin')

plt.show()
'''

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.0, 22105.3]

#plt.plot(years, gdp, color='blue', marker = 'o', linestyle='dotted')   #plot는 라인 차트를 의미!
# 막대 차트 만들기(bar)
plt.bar(range(len(years)), gdp) #(가로 범위, 세로 막대)  * 범위로 지정하게 되면 가로축의 값을 바꿔줘야한다!(xticks)
plt.title("GDP FOR YEAR")
plt.ylabel("Dollars")
plt.xlabel("Years")

# 가로축 범위 바꾸기
plt.xticks(range(len(years)), years)

plt.savefig("./Python_Basic/test.png", dpi = 600)
plt.show()