# map, filter 함수
'''
map 함수 사용방법
-> map(함수, 순서가 있는 자료형)    # 순서가 있는 자료형 [] : 리스트, {} : 딕셔너리, () : 튜플

ex> map(int, ['1','2','3','4','5'])   # int 함수는 정수형으로 변환해주는 함수

['1','2','3','4','5'] -> int -> map object (1,2,3,4,5)

map object를 리스트로 변환하여 사용
-> list(map(함수, 순서가 있는 자료형))
list(map(int, ['1','2','3','4','5']))


map 함수 활용 예
- 리스트의 모든 요소의 공백 제거

for문 활용 시
items = [' 로지텍마우스 ', ' 앱솔키보드 ']
for i in range(len(items)) :
    items[i] = items[i].strip()

map 함수 사용 시
def strip_all(x) :
    return x.strip()

items = [' 로지텍마우스 ', ' 앱솔키보드 ']

items = list(map(strip_all, items))

함수는 lambda 함수로 대체 가능!
items = list(map(lambda(x : x.strip(), items)))


filter 함수 사용방법
-> filter(함수, 순서가 있는 자료형)
def func(x) :
    return x<0
filter(func,[-3,-2,0,5,7])

[-3,-2,0,5,7] -> x<0 ? -> filter object (-3, -2)

filter object를 리스트로 변환하여 사용

filter 함수 활용 예
- 리스트의 길이가 3 이하인 문자들만 필터링

for문 사용 시
animals = ['cat', 'tiger', 'dog', 'bird', 'monkey']
result = []
for i animals :
    if len(i) <= 3 :
        result.append(i)

filter 함수 사용 시
def leng_under_3(x) :
    return len(x)<=3
result = list(filter(leng_under_3, animals))

람다 함수 적용 시
result = list(filter(lambda x : len(x)<=3, animals))
'''

# map 함수
'''
사용하는 이유
- 기존 리스트를 수정하여 새로운 리스트를 만들기 위해 사용

사용 방법
map(함수, 순서가 있는 자료형)
'''
print(list(map(int, ['3','2','1','5','4'])))

# 예제 - 리스트의 모든 요소의 공백 제거
items = ['  a  ', ' b ', 'c   ', '   d']
print(list(map(lambda x : x.strip(), items)))


# filter 함수
'''
사용하는 이유
- 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때
'''
def func(x) :
    return x<0
print(list(filter(func, [-3,-2,0,5,7])))

# 예제 - 리스트에서 길이가 3 이하인 문자들만 출력
items = ['pencil', 'scissors', 'ruler', 'pen']
print(list(filter(lambda x : len(x)<=3, items)))