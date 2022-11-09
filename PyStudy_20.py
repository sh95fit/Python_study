# 클래스 - 오버라이딩, 클래스 변수, private 변수
'''
클래스 변수
인스턴스들이 모두 공유하는 변수

private 변수
클래스 내부에서만 사용되는 변수
선언 - 변수, 함수 앞에 "__"를 붙여 선언 (언더바 2개!  언더바 1개는 Protected, 생략 시 Public)
ex> __PrivateVariable(self)  /함수인 경우   | __privatevariable = 0 /변수인 경우
불가피한 경우 클래스 외부에서 사용할 수 있다
형태 : _클래스명 + 변수 이름
ex> _PrivateVariable.__privatevariable
'''

import random

# 오버라이딩

# 부모 클래스
class Monster:
    max_num = 1000
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1    # 클래스 변수

    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스


class Wolf(Monster):
    pass


class Shark(Monster):
    def move(self):        # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")


class Dragon(Monster):
    def __init__(self, name, health, attack):    # 생성자 오버라이딩
        super().__init__(name, health, attack)           # 상속받은 부모클래스를 받아오는 함수 : super()
#        self.skills = skills         # 매개변수에 skill을 추가할 경우
        self.skills = ("불뿜기", "꼬리치기", "날개치기") # 매개변수를 간단하게 할 경우
    def move(self):         # 메서드 오버라이딩
        print(f"[{self.name}] 날기")
    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}")


wolf = Wolf("늑대", 1500, 210)
print(wolf.max_num)
wolf.move()

shark = Shark("상어", 3000, 400)
print(shark.max_num)
shark.move()

dragon = Dragon("용", 5000, 500)
print(dragon.max_num)
dragon.move()

dragon.skill()