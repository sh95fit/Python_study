#클래스와 객체
'''
클래스와 객체의 개념
클래스 - 객체를 만들기 위한 설계도
객체 - 설계도로부터 만들어낸 제품

# 클래스 활용 vs 비활용 비교

클래스를 사용하지 않은 경우 예시

champion1_name = '이즈리얼'
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

champion2_name = '리신'
champion2_health = 800
champion2_attack = 95

print(f"{champion3_name}님 소환사의 협곡에 오신 것을 환영합니다.")

champion3_name = '야스오'
champion3_health = 600
champion3_attack = 80

print(f"{champion2_name}님 소환사의 협곡에 오신 것을 환영합니다.")

def basic_attack(name, attack) :
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)
basic_attack(champion3_name, champion3_attack)

-----------------------------------------------------------------------

클래스를 사용하는 경우

class Champion :
    def __init__(self, name, health, attack) :
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사의 협곡에 오신 것을 환영합니다.")
    def basic_attack(self) :
        print(f"{self.name} 기본 공격 {self.attack}")

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 90)
yasuo = Champion("야스오", 600, 80)
ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()

즉! 클래스 사용 주 목적은 코드 간소화에 있다.

클래스의 구성 (클래스는 속성, 메서드의 집합!)
- 속성, 메서드
속성 - 특징을 나타냄
메서드 - 동작을 나타냄

class 정의

class 클래스이름 :
    def 메서드이름(self) :
        명령 블록

class 호출

인스턴스 = 클래스이름()
인스턴스.메서드()   #메서드 사용

인스턴스 - 클래스와 연관지어 사용할 때 사용되는 용어(객체와 유사)

Tip! 파이썬에서는 자료형도 클래스이다!
'''

class Monster :
    def say(self) :
        print("나는 몬스터다!")

goblin = Monster()
goblin.say()

# 파이썬에서는 자료형도 클래스다
a = 10
b = "문자열객체"
c = True

print(type(a))
print(type(b))
print(type(c))

# 문자열에서 사용할 수 있는 메서드 확인 - .__dir__() 활용
print(b.__dir__())
