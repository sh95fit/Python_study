# 튜플
'''
튜플의 특징
1. 시퀀스 자료형이다
2. 수정, 추가, 삭제가 불가능한 리스트! 즉 읽기 전용!
  - 읽기 전용을 사용하는 이유 : 메모리 사용이 효율적이기 때문!!
3. 메모리 사용이 효율적
4. 읽기만 가능하므로 데이터 손실 위험이 적다

튜플 = (데이터, 데이터, 데이터)    / 튜플은 소괄호를 쓴다!
튜플 = 데이터, 데이터 데이터    / 튜플은 소괄호를 생략할 수 있다!!!

Tip! 괄호 형태별 구분
() : 함수, 튜플
[] : 리스트 정의, 인덱스
{} : fstring, 딕셔너리

튜플 예시
a = (3, 4, 5)
a = "문자열", 숫자, 논리(True)      / 데이터의 자료형이 동일하지 않아도 된다!

1개의 데이터를 가지는 튜플을 생성할 경우
변수 = (데이터, )
변수 = 데이터,           / 콤마를 반드시 표기해주어야 한다!

리스트를 튜플로 만드는 방법!
a = tuple([5,6,7])   / 자료형의 변환!(리스트 -> 튜플) 
  => [5,6,7] -> (5,6,7)

x = list(range(10))   / 0~9까지 숫자를 가진 객체를 리스트로 반영 [0,1,2,3,4,5,6,7,8,9]
a = tuple(x)   / 리스트를 튜플로 만듦 (0,1,2,3,4,5,6,7,8,9)

x = 5,6,7
a = list(x)      / 튜플 또한 리스트로 변경할 수 있다!

패킹 & 언패킹  (튜플과 동일하게 리스트도 패킹, 언패킹 적용 가능!)
number = 3,4,5    /패킹 - 튜플 형태로 변수에 저장(묶음) 
3,4,5 = number    /언패킹 - number는 현재 (3,4,5) 이므로 이를 a,b,c에 각각 매칭되서 반영됨  a <= 3, b <= 4, c <= 5

패킹 : 여러 개의 데이터를 하나의 변수에 할당하는 것
언패킹 : 컬렉션의 각 데이터를 각각의 변수에 할당하는 것

튜플 함수 활용 (리스트도 동일하게 적용 가능)
ex> a = 10,20,30,40,30

1. 특정값의 인덱스 구하기    :    a.index(20)   -> 1
2. 특정값의 개수     :    a.count(30)      -> 2
3. 최대값, 최소값    :    max(a), min(a)   -> 40, 10
4. 합계    :    sum(a)   -> 130
'''

# 튜플 실습

a = (3, 4, 5)
b = 3, 4, 5
c = (3, )
d = 3,
e = tuple([3,4,5])

f = list(range(9))
g = tuple(f)

h = 3, 4, 5
i = list(h)

# 튜플 관련 함수
x = 5, 6, 7, 8
print(max(x))
print(min(x))
print(sum(x))
print(x.count(6))
print(x.index(7))