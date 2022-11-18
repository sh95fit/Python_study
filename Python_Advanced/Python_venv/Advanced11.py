# 클래스의 여러가지 메서드
'''
인스턴스 메서드(instance method)
인스턴스 속성에 접근할 수 있는 메서드
항상 첫 번째 파라미터로 self를 갖는다.


클래스 메서드(class method)
클래스 속성에 접근하기 위해서 사용한다.
클래스를 의미하는 cls를 파라미터로 받는다.

ex>
class Unit :
    count = 0
    ...
    @classmethod  # 데코레이터
    def print_count(cls) :   # cls 파라미터로 받음
        print(f"전체 유닛의 수 : {cls.count}")    #cls.속성명 형태로 호출

정적 메서드(static method)
인스턴스를 만들 필요가 없는 메서드
self를 받지 않는다
메서드가 인스턴스 유무와 관계없이 독립적으로 사용될 때 적용

ex>
class Math :
    @staticmethod
    def add(x.y) :
        return x, y

매직 메서드(magic method)
클래스 안에서 정의할 수 있는 스페셜 메서드
특별한 상황에 호출된다.   
__이름__의 형태로 되어있다.   # __init__ 메서드도 매직 메서드에 포함됨!
'''




'''
인스턴스 메서드 만들기

hit 메서드 구현
데미지를 받으면 체력과 방어막이 깎이는 hit 메서드를 구현해보자

1. 데미지가 방어막보다 작거나 같으면 방어막만 깎인다.
2. 데미지가 방어막보다 크고 체력보다 작으면 체력과 방어막이 깎인다.
3. 데미지가 체력보다 크면 체력을 0으로 만든다.
'''

class Unit :
    count = 0   # 클래스 속성
    def __init__(self, name, hp, shield, damage) :  # 매직 메서드 - 객체 생성 시 호출
        self.name = name
        self.hp = hp
        self.shield =shield
        self.damage = damage
        Unit.count += 1
        print(f"[{self.name}](이)가 생성되었습니다.")

    def __str__(self) :  # 매직 메서드 - 출력 시 호출
        return f"[{self.name}] 체력 : {self.hp} 방어막 : {self.shield} 공격력 : {self.damage}"
  
    # 인스턴스 메서드    *인스턴스 : 메모리상 객체의 실체
    def hit(self, hit_damage) :
        self.hit_damage = hit_damage

        if  self.hit_damage <= self.shield :
            self.shield -= self.hit_damage
            print(f"[{self.name}]님의 방어막이 {self.hit_damage}만큼 감소하였습니다.")
            self.hit_damage = 0
        elif self.hit_damage > self.shield and (self.hit_damage-self.shield) < self.hp :
            self.hit_damage -= self.shield
            self.shield = 0
            self.hp -= self.hit_damage
            print(f"[{self.name}]의 방어막이 파괴되었습니다.")
            print(f"[{self.name}]의 체력이 {self.hit_damage}만큼 감소하였습니다.")
            self.hit_damage = 0
        elif self.hit_damage > self.shield and (self.hit_damage-self.shield) > self.hp :
            self.shield = 0
            self.hp = 0
            print(f"[{self.name}]이 사망하였습니다.")
            self.hit_damage = 0
            self.damage = 0

    # 클래스 메서드 - 클래스 속성에 접근하는 메서드
    @classmethod    # 데코레이터
    def print_count(cls) :
        print(f"생성된 유닛 : [{cls.count}] 개")


probe = Unit("프로브", 20, 20, 5)
zealot = Unit("질럿", 100, 60, 16)
dragoon = Unit("드라군", 100, 80, 20)

#인스턴스 메서드 호출
probe.hit(50)
print(probe)

#클래스 메서드 호출
Unit.print_count()




# 정적 메서드
class Math : 
    # 정적 메서드(Static method)
    # 인스턴스를 만들 필요가 없는 메서드
    @staticmethod
    def add(x, y) :
        return x + y

    @staticmethod
    def sub(x, y) :
        return x - y

# 정적 메서드로 되어있는 경우 인스턴스를 만들 필요가 없다.
# 정적 메서드 호출
print(Math.add(4,5))
print(Math.sub(5,4)) 



# 객체가 가진 메서드, 함수를 확인하는 함수 : dir(객체)
print(dir(probe))