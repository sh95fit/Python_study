# 제너레이터
'''
* 제너레이터란?
 - 이터레이터를 만드는 함수
 
* 제너레이터 생성 방법
 - 함수에서 yield를 사용하면 된다!

* 제너레이터 특징
 1. 함수 안에서 yield를 사용한다
 2. 제너레이터 표현식을 사용할 수 있다.
 3. 메모리 사용이 효율적이다.
   : 리스트 : 데이터 저장에 필요한 메모리를 모두 사용
     제너레이터 : 나중에 필요한 경우에 값을 만들어 사용 (메모리가 적게 소모!)

* 제너레이터는 이터레이터 범주에 포함되는 것
 - 즉, 이터레이터 > 제너레이터

* 제너레이터 표현식
 - 제너레이터 <- 리스트 내포와 유사 []를 ()로만 바꿔주면 된다!

'''

def season_generator(*args) :
    for arg in args :
        yield arg   # arg 값을 리턴하고 함수 실행을 잠시 지연시킴 - 다음 arg 값이 들어오면 해당 값을 리턴하고 다시 함수 실행을 지연시킴 // 범위가 끝나면 StopIteration 에러 발생

g = season_generator('spring', 'summer', 'autumn', 'winter')
print(dir(g))   # __iter__ 존재 확인

print(g.__iter__())

print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
#print(g.__next__())    # 에러 확인



def func() :
    print("첫번째 작업중 ... ")
    yield 1                     # return을 쓰게 되면 한 개의 값을 반환하고 함수가 종료된다!
                                # yield를 활용하면 작업을 나눠서 실행할 수 있다.
    print("두번째 작업중 ... ")
    yield 2

    print("세번째 작업중 ... ")
    yield 3

ge = func()

data = ge.__next__()
print(data)
data = ge.__next__()
print(data)
data = ge.__next__()
print(data)


# 제너레이터 표현식
# 제너레이터 <- 리스트 내포와 유사 []를 ()로만 바꿔주면 된다!

double_generator = (i * 2 for i in range(1,10))

print(double_generator)

for i in double_generator :
    print(i)


# 메모리 효율이 왜 좋은가?  
# ex> 숫자 1 - 10000을 3배로 만든 결과 (리스트 vs 제너레이터)

list_data = [i*3 for i in range(1,10000+1)]
generator_data = (i*3 for i in range(1,10000+1))

# 메모리 사용 정도 확인
import sys

print(sys.getsizeof(list_data))     # 단위 : 바이트
print(sys.getsizeof(generator_data))    # 결과값을 저장하지 않고 __next__()가 호출될 때 결과값을 만듦

# 리스트 : 데이터 저장에 필요한 메모리를 모두 사용
# 제너레이터 : 나중에 필요한 경우에 값을 만들어 사용 (메모리가 적게 소모!)