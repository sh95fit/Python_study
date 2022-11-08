# 스택 구조
'''
FILO : 먼저 들어간 데이터가 나중에 나옴
FIFO : 먼저 들어간 데이터가 먼저 나옴
'''

# 리스트 활용 스택 클래스 만들기
class Stack(object) :    # object : 숫자, 문자 상관 없이 받을 수 있음
    def __init__(self) :
        self.stack = []
    def push(self, item) :
        self.stack.append(item)
    def pop(self) :     
        self.stack.pop()     #list에서 빼는 방법! pop   == remove, del 과 동일한 기능
    def size(self) :
        return len(self.stack)
    def printStack(self) :
        for i in self.stack :
            print(i)
    def show(self):
        return self.stack;
    

stack = Stack()

print(stack.size())
stack.push(10)
stack.push(20)
stack.push(30)
stack.printStack()
print(stack.size())
stack.pop()
print(stack.show())
stack.pop()
print(stack.show())
stack.push(3)
print(stack.show())
print(stack.size())
stack.printStack()


