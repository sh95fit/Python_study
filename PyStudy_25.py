# 파일 입출력 기초
'''
pickle 모듈
파이썬 설치 시 자동으로 설치되는 내장 모듈

파일에 파이썬 객체 저장
ex> 
    import pickle  
    data = {
        "목표1" : "팔굽혀펴기 100회",
        "목표2" : "Python 공부"
    }
    file = open("data.pickle", "wb")     # wb : 쓰기 바이너리 모드(컴퓨터가 바로 읽을 수 있는 데이터 형식)
    pickle.dump(data,file)
    file.close()

파일로부터 파이썬 객체 읽기
    import pickle
    file = open("data.pickle", "rb")     # rb : 읽기 바이너리 모드
    data = pickle.load(file)
    print(data)
    file.close()


with 구문
close() 함수를 생략할 수 있다
with 구문 뒤 자동으로 close() 처리

with 구문 미사용 시
file = open("data.txt", "r")
data = file.read()
file.close()

with 구문 사용 시
with open("data.txt","r") as file :
    data = file.read()


csv 파일 입출력 
csv 모듈은 파이썬 내장 모듈!

csv 파일이란(comma-separated values)
데이터가 콤마로 구분된 텍스트 파일 형식
테이블 형태의 데이터를 표시하기 위해 csv 파일을 활용

csv 파일 쓰기
ex>
import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형톤", 5, 32]
]

file = open("test.csv", "w")
writer = csv.writer(file)
for d in data :
    writer.writerow(d)
file.close()

csv 파일 읽기
ex>
improt csv

file = open("test.csv", "r")
reader = csv.reader(file)
for d in reader :
    print(d)
file.close()
'''

# 1. 파이썬 객체를 pickle로 저장
import pickle

data = {
        "목표1" : "팔굽혀펴기 100회",
        "목표2" : "Python 공부"
}

file = open("data.pickle", "wb")
pickle.dump(data,file)
file.close()

# 2. pickle 파일을 파이썬으로 load
file = open("data.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()



# with 구문
with open("data.txt", "r", encoding = "UTF-8") as file :
    data = file.read()
    print(data)



# csv 파일 입출력
import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형톤", 5, 32]
]

file = open("test.csv", "w", newline="", encoding = "UTF-8-SIG")    # newline : 윈도우를 쓰게 되면 자동으로 한 줄씩 띄워쓰기가 적용되는데 이를 적용하지 않기 위해 사용
writer = csv.writer(file)

for d in data :
    writer.writerow(d)   # 리스트에 저장된 파일을 1줄씩 쓰기

file.close()

# csv 파일 읽기
file = open("test.csv", "r", encoding="UTF-8-SIG")
reader = csv.reader(file)
for data in reader :
    print(data)
file.close()