# 함수
'''
함수를 사용하는 이유?
- 재사용성이 좋아진다
- 유지보수가 편리하다
- 가독성이 좋아진다

- 매개변수가 없는 기본형
* 정의하기
def 함수이름() :  
    명령 블록

* 호출하기
함수이름()


- 매개변수가 있는 형태
* 정의하기
def 함수이름(매개변수1, 매개변수2) :  /매개변수 개수는 상관 없음!
    명령 블록

* 호출하기
함수이름(인자1, 인자2)

- 반환값이 있는 함수
* 정의하기
def 함수이름(매개변수1, 매개변수2) : /매개변수가 없는 경우 ()
    명령블록
    return 반환값

* 호출하기
함수이름(인자1, 인자2) / 매개변수가 없는 경우 ()
'''

# 기본형
def printHello() :
    print("Hello!!")

printHello()

# 매개변수가 있는 함수형
def sum(a, b) :
    print(a+b)

sum(10, 2)

# 반환값이 있는 함수
import random
def getRandomNumber() :
    number = random.randint(1, 100)
    return number

print(getRandomNumber())


# 매개변수와 반환값이 있는 함수
def add(a, b) :
    result = a + b
    return result

print(add(5, 6))