# 람다 함수
'''
람다 함수란?
이름을 지을 필요도 없는 간단한 형태의 함수
다른 함수의 인자(argument)로 넣을 수 있다.
코드가 간결해지고, 메모리가 절약된다.

람다 함수 정의 방법
lambda 매개변수 : 결과
lambda a : a-1

람다 함수 호출 방법
첫번째 방법
(lamda a : a-1)(매개변수)
두번째 방법
변수 = lambda a : a-1
변수(매개변수)

람다 함수 사용법(if문)
주의사항 : 항상 else까지 같이 써줘야 한다!
lambda a : True if a>0 else False
'''

# 기존함수 사용 시
def minus_one(a) :
    return a-1

# 람다 함수
lambda a : a-1

# 람다 함수 호출 - 함수 자체 호출
print((lambda a : a-1)(10))
# 람다 함수 호출 - 변수에 대입하여 호출
num = lambda a : a-1
print(num(100))


# 람다 함수에서 if문 사용

# 기존함수 사용 시
def is_positive_number(a) :
    if a > 0 :
        return True
    else :
        return False

# 람다 함수
lambda a : True if a>0 else False

# 함수 자체 호출
print((lambda a : True if a>0 else False)(10))
# 변수에 대입하여 호출
num = lambda a : True if a>0 else False
print(num(-1))
