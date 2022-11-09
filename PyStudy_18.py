# 생성자(__init__) 함수, self란?, 속성&메서드 추가방법
'''
클래스
- 속성, 메서드 2가지 요소 필요
- 속성은 특징을 나타냄
- 메서드는 동작을 나타냄

예제
class Monster :
    def __init__(self, health, attack, speed) :   # self는 매개변수로 반영되지 않음!
        self.health = health
        self.attack = attack
        self.speed = speed

goblin = Monster(800,120,300)  # 해당 시점에서 __init__ 함수가 호출됨  / self는 goblin 인스턴스 자기자신을 의미
wolf = Monster(1500,200,350)  # 해당 시점에서 __init__ 함수가 호출됨  / self는 wolf 인스턴스 자기자신을 의미

__init__ : 인스턴스를 만들 때 반드시 호출되는 함수! (가장 먼저 호출되는 함수)
self : 인스턴스 자기 자신을 뜻함!

메서드 추가

예제
class Monster :
    def __init__(self, health, attack, speed) :   # self는 매개변수로 반영되지 않음!
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self,num) :      # 메서드 추가
        self.health -= num
    def get_health(self) :               # 메서드 추가
        return self.health

goblin = Monster(800,120,300)
wolf = Monster(1500,200,350)
goblin.decrease_health(100)
print(goblin.get_health())
'''

# 생성자 - 인스턴스를 만들 때 호출되는 메서드
# 객체는 인스턴스를 포함하는 형태 / 인스턴스는 객체가 만들어지는 시점의 객체


class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self, num) : 
        self.health -= num
    def get_health(self):
        return self.health

# 고블린 인스턴스 생성
goblin = Monster(800, 120, 300)


goblin.decrease_health(100)
print(f"남은 체력 : {goblin.get_health()}")


# 새로운 인스턴스 생성
wolf = Monster(1500, 200, 350)

wolf.decrease_health(300)
print(f"남은 체력 : {wolf.get_health()}")
