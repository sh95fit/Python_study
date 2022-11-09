# 클래스 - 상속
'''
상속의 개념
부모클래스 - 자식 클래스
부모클래스 - 속성, 메서드
자식클래스는 부모클래스에 존재하는 속성, 메서드를 그대로 가져와 사용할 수 있다!

클래스들의 중복된 코드를 제거하고 유지보스를 용이하게 하기 위해 사용!

예시

부모 클래스
class Monster :
    def __init__(self, name, health, attack) :
        self.name = name
        self.health = health
        self.attack = attack
    def move(self) :
        print("지상에서 이동하기")


자식 클래스
class Wolf(Monster) :          # (Monster) 부분이 부모 클래스를 상속 받는 부분
    pass                       # 부모 클래스의 속성, 메서드만 사용 가능

class Shark(Monster) :
    def move(self) :           # Shark 클래스에서만 추가된 속성, 메서드   ** 메서드 오버라이딩
        print("헤엄치기")      

class Dragon(Monster) :
    def move(self) :           # Dragon 클래스에서만 추가된 속성, 메서드
        print("날기")           

'''


# 상속

# 부모 클래스
class Monster :
    def __init__(self, name, health, attack) :
        self.name = name
        self.health = health
        self.attack = attack
    def move(self) :
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster) :
    pass

class Shark(Monster) :
    def move(self) :        # 메서드 오버라이딩
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster) :
    def move(self):         # 메서드 오버라이딩
        print(f"[{self.name}] 날기")


wolf = Wolf("늑대", 1500, 210)
wolf.move()
shark = Shark("상어", 3000, 400)
shark.move()
dragon = Dragon("용", 5000, 500)
dragon.move()