# 클래스와 객체
'''
* 절차지향 vs 객체지향
절차 지향 프로그래밍
- 기능들을 어떤 순서로 처리할 것인가에 초점을 맞춘다.
- 프로그램의 규모가 작은 경우

객체 지향 프로그래밍
- 객체가 중심이 되고, 객체를 정의하고 객체간 상호작용에 초점을 맞춘다.
- 프로그램의 규모가 큰 경우



* 클래스와 객체의 개념
클래스
- 객체를 만들기 위한 설계도
- 속성, 메서드로 구성

객체
- 설계도(클래스)로부터 만들어낸 제품



* 클래스 만들기
클래스 형태
class 클래스이름 :
    pass

* 객체 만들기
객체 형태
인스턴스 = 클래스이름()

* 속성 추가하기
클래스 내 속성 반영 형태
-> 속성은 보통 생성자(__init__)를 통해 추가
형태
class 클래스명 :
    def __init__(self, 속성1, 속성2, 속성3)
        self.속성1 = 속성1
        self.속성2 = 속성2
        self.속성3 = 속성3

속성 부여하는 방법
인스턴스 = 클래스명(속성1, 속성2, 속성3)

* 메서드 추가하기
class 클래스명 :
    def __init__(self, 속성1, 속성2, 속성3)
        self.속성1 = 속성1
        self.속성2 = 속성2
        self.속성3 = 속성3
    def __str__(self) :
        print(f"{self.속성1}, {self.속성2}, {self.속성3}")

인스턴스 = 클래스명(속성1, 속성2, 속성3)

print(인스턴스)
'''

# Unit 클래스
class Unit :
    '''
    속성 : 이름, 체력, 방어막, 공격력
    '''

    # 생성자(constructor)
    # 객체를 생성할 때 호출되는 메서드
    def __init__(self, name, hp, shield, damage) :
        self.name = name
        self.hp = hp
        self.shield =shield
        self.damage = damage
        print(f"[{self.name}](이)가 생성되었습니다.")

    # 객체를 출력할 때 호출되는 메서드
    def __str__(self) :
        return f"[{self.name}] 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.damage}"

# 프로브 객체 생성
Probe = Unit("프로브", 20, 20, 5)

# 질럿 객체 생성
Zealot = Unit("질럿", 100, 60, 16)

# 드라군 객체 생성
Dragoon = Unit("드라군", 100, 80, 20)

# 객체의 속성 정보를 출력
print(Probe)
print(Zealot)
print(Dragoon)