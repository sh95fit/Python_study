# 모듈 만들기 실습
'''
# 결제 정보 관리 모듈
'''
# 변수
version = 2.0

# 함수
def printAuthor() :
    print("test")

# 클래스
class Pay :
    def __init__(self, id, price, time) :
        self.id = id
        self.price = price
        self.time = time
    def get_pay_info(self) :
        return f"{self.time} {self.id} {self.price}"

#해당 파일을 직접 실행 했을 때만 실행된다.
#즉 다른 파일에서 실행 시에는 __main__이 아닌 모듈이름이 출력된다.
if __name__ == "__main__":
    print("pay module 실행")

print(__name__)
