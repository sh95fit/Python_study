# 함수
'''
def 함수명(입력인수[, 입력인수[, 입력인수]]) :
    문장
    return 변수명(또는 값)
'''

# 최댓값 비교

def max(x, y) :
    if x > y :
        return x
    elif x < y :
        return y
    else :
        return '비교 불가'

a = int(input("숫자1 = "))
b = int(input("숫자2 = "))

result = max(a,b)
print(result)


# 사칙연산 함수 이용
'''
def plus(x, y) :
    return x + y

def minus(x, y) :
    return x - y

def mul(x, y) :
    return x * y

def div(x, y) :
    return x / y
'''

'''
함수, 포맷 활용
'''

def plus(x, y) :
    print('{0} + {1} = {2}'.format(x, y, x+y))

def minus(x, y) :
    print('{0} - {1} = {2}'.format(x, y, x-y))

def mul(x, y) :
    print('{0} * {1} = {2}'.format(x, y, x*y))

def div(x, y) :
    print('{0} / {1} = {2}',format(x, y, x/y))

def calc(x,y,op) :
    if(op == '+') : plus(x,y)
    if(op == '-') : minus(x,y)
    if(op == '*') : mul(x,y)
    if(op == '/') : div(x,y)

a = int(input("숫자1 = "))
op = input("연산자 = ")
b = int(input("숫자2 = "))

print(calc(a,b,op))


'''
구구단
'''

def gugudan(n) :
    for i in range(1,10) :
        print('{0} * {1} = {2}'.format(n, i, (n*i)))

# gugudan(2)

n = int(input("출력할 구구단 : "))
gugudan(n)

