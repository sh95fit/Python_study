# 리스트 자료형

'''
리스트를 사용하는 이유
-> 여러 개의 변수를 지정해야하는 경우 반복적인 지정을 피하기 위해 사용

리스트 형태
리스트명 = [데이터, 데이터, ... , 데이터]

데이터 접근하기
-> 인덱스 사용
  리스트명[0] ~ ...

데이터 조작하기
-> 데이터 추가
  리스트.append(데이터)
-> 데이터 할당(변경 등)
  리스트[인덱스] = 데이터
-> 데이터 삭제
  del 리스트[인덱스]

-> 리스트 슬라이싱
  리스트[시작 : 끝+1]

-> 리스트 길이
  len(리스트)

-> 리스트 정렬
  리스트.sort() 
  리스트.sort(reverse = True) # 역순
'''

# 1. 리스트 만들기
# - 데이터가 있는 리스트
animals = ["고양이", "강아지", "돼지", "소"]

# - 데이터가 없는 리스트
empty = []

# 2. 리스트 조작하기
# - 데이터 접근하기
# 인덱스는 0부터 시작
print(animals[2])
print(animals[-1])

# - 데이터 추가하기
animals.append("고라니")
print(animals)

# - 데이터 할당하기
animals[1] = "청개구리"
print(animals)

# - 데이터 삭제하기
del animals[1]
print(animals)

# - 리스트 슬라이싱
print(animals[1:3])
print(animals[:]) # 전체
print(animals[:3])
print(animals[1:])

# - 리스트 길이
print(len(animals))

# - 리스트 정렬
animals.sort()
print(animals)
animals.sort(reverse = True)
print(animals)