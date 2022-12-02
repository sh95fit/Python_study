# 데코레이터
'''
* 데코레이터란?
 - 함수의 앞, 뒤로 부가적인 기능을 넣어주고 싶을 때 사용 (앞, 뒤 중 필요한 부분에만 넣어줄 수도 있음)
 - ex> 로깅(프로그램 실행시 로그를 남기는 일련의 작업), 권한확인 작업 시 주로 사용

* 데코레이터 생성 방법
 - 클로저를 이용해서 생성
 - 적용하고 싶은 함수 앞에 '@데코레이터' 형태로 적용
'''


# 데코레이터를 사용하지 않는 경우

def print_hello() :
    print("함수 시작")
    print("hello Python_Study")
    print("함수 끝")

def print_bye() :
    print("함수 시작")      # 중복되는 부분이 발생
    print("bye Python_Study")
    print("함수 끝")        # 중복되는 부분이 발생


# 중복을 제거하기 위해 데코레이터 사용!

# 데코레이터를 사용하는 경우

def logger(func) :
    def wrapper(*arg) :
        print("함수 시작")
        func(*arg)  # 함수 실행
        print("함수 끝")
    return wrapper

@logger
def print_hello(name) :
    print("hello ", name)

@logger
def print_bye(name, age) :
    print("bye ", name, age)


print_hello('Python_Study')
print_bye('Python_Study', '20')