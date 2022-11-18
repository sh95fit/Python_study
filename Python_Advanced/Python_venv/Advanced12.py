# 상속
'''
상속의 개념
클래스들의 공통된 속성과 메서드를 뽑아내서 부모클래스를 만든다!
이를 자식이 상속 받아 사용한다.

상속의 장점
코드의 중복을 제거할 수 있다.
유지보수가 편리해진다.

상속 받는 방법
class 자식클래스이름(부모클래스이름) :  형태로 상속
 
추상클래스
추상 메서드를 가지는 클래스
추상 메서드
상속받는 자식 클래스에서 구현을 강제하도록 만든 메서드
추상클래스를 사용하려면 abc 모듈을 사용해야한다!
from abc import *
'''

# 상속 실습 - 게임 아이템 활용
# 부모 클래스 - Item / 자식 클래스 - Weapon, HealingItem / 추상 클래스 - 추상메서드(사용하기)

# 추상 클래스 이용하기!
# 추상클래스를 이용할 때에는 abc라는 모듈을 import해줘야 한다.
from abc import *


class Item(metaclass = ABCMeta) :   # metaclass = ABCMeta 반영시 추상클래스로 적용됨!
    '''
    속성 : 이름
    메서드 : 줍기, 버리기
    '''
    def __init__(self, name) :
        self.name = name

    def pick(self) :
        print(f"[{self.name}]를(을) 주웠습니다.")

    def discard(self) :
        print(f"[{self.name}]를(을) 버렸습니다.")
    
    @abstractmethod
    def use(self) :
        print("공격 완료")

class Weapon(Item) :
    '''
    속성 : 공격력
    메서드 : 공격하기
    '''
    def __init__(self, name, damage) :
        super().__init__(name)
        self.damage = damage

    def attack(self) :
        print(f"[{self.name}]를(을) 이용해 {self.damage}만큼 데미지를 입혔습니다.")
    
    def use(self) :
        print("공격 완료")

class HealingItem(Item) :
    '''
    속성 : 회복량
    메서드 : 사용하기
    '''
    def __init__(self, name, recovery_amount) :
        super().__init__(name)
        self.recovery_amount = recovery_amount

    def recovery(self) :
        print(f"[{self.name}]를(을) 사용해 {self.recovery_amount}만큼의 체력을 회복하였습니다.") 
    
    def use(self) :
        print("회복 완료") 


m16 = Weapon("m16", 110)
bandage = HealingItem("붕대", 50)

m16.attack()
m16.use()
bandage.recovery()
bandage.use()

