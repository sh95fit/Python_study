# 클래스 기초
'''
python의 특징
1. 인터프리터 - 위에서 순차적으로 아래로 내려가면서 1줄씩 해석(에러가 나는 경우 바로 표시)

다른 언어와의 차이
javascript : 에러가 발생해도 순차적으로 전체 해석 진행
c, c++ : 컴파일러를 활용한 해석(속도가 빠름)

2. 객체 지향 언어!
-> class
 소스가 너무 길어질 경우 찾기가 힘들어짐
 기능별 구분을 클래스 형태로 구성하여 소스를 간소화

클래스는 호출 시 다른 변수에 지정하여 메모리상 별도로 생성이 가능!

self를 통해 가상의 변수를 지정할 수 있음!

생성자! -> def __init__ :    / __init__ 형태로 지정 - 클래스 호출 시 1회 실행되는 부분

Tip! 클래스의 첫 글자를 대문자로 표시해 구분해면 좋음

# 클래스 정의 방법
class ClassName : 
    #변수
    #함수
    title = "Hello Python"

# 클래스 사용 방법
변수 = ClassName()
print(변수.title)

'''

'''
# 클래스 테스트
class ClassName : 
    #변수
    #함수
    title = "Hello Python"


p1 = ClassName()
print(p1.title)
'''

# 계산기 예시
'''
class Calculator :
    def setNum(self, n1, n2) :      # self는 가상의 변수를 생성해줌 / Java의 this와 비슷한 개념
        self.num1 = n1
        self.num2 = n2

    def plus(self) :
        return self.num1 + self.num2
    def minus(self) :
        return self.num1 - self.num2
    def mul(self) :
        return self.num1 * self.num2
    def div(self) : 
        return self.num1 / self.num2


cal = Calculator()
n1 = int(input("숫자1 >>> "))
n2 = int(input("숫자2 >>> "))
cal.setNum(n1,n2)
print(cal.plus())
print(cal.minus())
print(cal.mul())
print(cal.div())
'''


# 누적되는 합산값 출력
class Calculator :
    def __init__(self) :        # 클래스 실행 시 기본적으로 1회 실행되는 함수
        self.result = 0
    def add(self, num) :
        self.result += num
        return self.result


cal = Calculator()
print(cal.add(3))
print(cal.add(4))


cal1 = Calculator()
print(cal1.add(4))
print(cal1.add(5))
