# 클로저
'''
* 내부 함수란?
 - 함수 안에 정의된 함수

* 클로저
 - 함수가 종료되어도 자원(변수)을 사용할 수 있는 함수

* 클로저가 될 수 있는 조건
 - 1. 내부 함수여야 한다
 - 2. 외부 함수의 변수를 참조해야 한다.
 - 3. 외부 함수가 내부 함수를 반환해야 한다.

* 클로저는 전역변수를 사용해서 대체는 가능하다
 But, 전역변수는 사용을 최소화하는 것이 좋다! (네이밍 문제, 스코프 문제 등이 발생할 수 있음)
 
 -> 클래스로도 대체가 가능함!

'''

# 내부 함수, 클로저 정의
def outer(name) :
    def inner() :
        print(name, "님 안녕하세요!")
    return inner

func = outer("Python_Study")    # outer 함수가 종료되었지만 클로저(closure) 공간 안에 name 변수가 저장되어있다.
func()

# 클로저
# 함수가 종료되어도 자원을 사용할 수 있는 함수

def greeting(name, age, gender) :
    def inner() :
        print(name, "님 안녕하세요!")
        print(f"나이 : {age}")
        print(f"성별 : {gender}")
    return inner

closure = greeting('홍길동', 29, 'male')
closure()

# 클로저가 저장되어 있는 위치 확인하기
print(dir(closure))     # __closer__ 튜플에 저장!
print(type(closure.__closure__))
print(dir(closure.__closure__[0]))  # cell_contents 

print(closure.__closure__[0].cell_contents) # cell_contents 내에 외부 함수의 변수 데이터를 갸지고 있다!

# 내용 전체 확인
for i in closure.__closure__ :

    print(i.cell_contents)

