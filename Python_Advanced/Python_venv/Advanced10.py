# 클래스의 여러가지 속성
'''
*인스턴스 속성(instance attribute)
객체마다 다르게 가지는 속성

클래스 내에서 인스턴스 속성 사용 시
self.속성명
클래스 밖에서 인스턴스 속성 사용 시
객체명.속성명

ex>
class 클래스명 :
    def __init__(self, 속성1, 속성2, 속성3)
        self.속성1 = 속성1    # 인스턴스 속성!
        self.속성2 = 속성2    # 인스턴스 속성!
        self.속성3 = 속성3    # 인스턴스 속성!


*클래스 속성(class attribute)
모든 객체가 공유하는 속성

클래스 밖에서 클래스 속성 사용 시
클래스명.속성명

ex>
class 클래스명 :
    속성 = 지정값  # 클래스 속성 생성
    def __init__(self, 속성1, 속성2, 속성3)
        self.속성1 = 속성1    # 인스턴스 속성!
        self.속성2 = 속성2    # 인스턴스 속성!
        self.속성3 = 속성3    # 인스턴스 속성!
        클래스명.속성 = 지정값    #클래스 속성!


*비공개 속성(private attribute)
클래스 안에서만 접근 가능한 속성
속성명 앞에 '__' 언더바 2개를 표시하면 클래스 밖에서는 접근 불가(즉, 변경이 불가능)
아예 접근이 안 되는 것은 아니며 접근이 어렵도록 만들어 놓은 속성!

비공개 속성에 접근하려면 네임 맹글링(anme mangling) 사용
'인스턴스._클래스명__속성' 형태로 접근 가능!

ex>
class 클래스명 :
    속성 = 지정값  # 클래스 속성 생성
    def __init__(self, 속성1, 속성2, 속성3)
        self.속성1 = 속성1    # 인스턴스 속성!
        self.__속성2 = 속성2    # 비공개 속성!
        self.속성3 = 속성3    # 인스턴스 속성!
'''

class Unit :
    '''
    인스턴스 속성 : name, hp, shield, damage
    -> 객체마다 다른 값을 가지는 속성
    클래스 속성 : count
    -> 모든 객체가 공유하는 속성

    비공개 속성
    -> 클래스 안에서만 사용 가능한 속성
    '''
    count = 0   # 클래스 속성
    def __init__(self, name, hp, shield, damage) :
        self.name = name
        self.__hp = hp
        self.shield =shield
        self.damage = damage
        Unit.count += 1
        print(f"[{self.name}](이)가 생성되었습니다.")

    # 객체를 출력할 때 호출되는 메서드
    def __str__(self) :
        return f"[{self.name}] 체력 : {self.__hp} 방어막 : {self.shield} 공격력 : {self.damage}"

probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)

# 클래스 밖에서 인스턴스 속성 접근 및 수정
probe.damage += 1
print(probe)

# 클래스 밖에서 클래스 속성 접근
print(Unit.count)

# 비공개 속성 접근 불가 확인
probe.__hp = 9999
print(probe)

# 네임 맹글링(name mangling)
probe._Unit__hp = 1000
print(probe)