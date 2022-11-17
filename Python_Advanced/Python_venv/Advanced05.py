# 할당과 복사
'''
* 파이썬에서는 데이터도 객체이다.
- 변수가 데이터를 가리킨다
  -> 즉, 데이터가 객체로 생성된 후 이를 가리키는 것이 변수이다. (변수 자체가 메모리 공간을 가지고 있는 것이 아니다!)

리스트(딕셔너리) 할당과 복사
리스트 할당 방식
ex> x = [1,2,3,4,5]
    y = x    # 여기서 y에 동일한 리스트가 복사되는 것이 아닌 같은 리스트 객체를 가리키도록 설정한 것!
               -> 즉, y와 x가 동일한 객체를 가리키고 있으므로 y를 수정하면 x 또한 수정된 객체를 가리키게 된다.

일차원 리스트 복사 방식
복사할 객체 = 복사될 객체.copy()

copy() 함수를 사용하면 동일한 객체가 복사되어 할당된다

ex> x = [1,2,3,4,5]
    y = x.copy()

다차원 리스트 복사 방식
import copy
복사할 객체 = copy.deepcopy(복사될 객체)
'''

# 리스트 할당 방식
x = [1,2,3,4,5]
y = x
y[2] = 0
print(x)
print(y)
print(id(x))     # 주소값 확인
print(id(y))

# 일차원 리스트 복사 방식
a = [5,6,7,8,9]
b = a.copy()
b[2] = 0
print(a)
print(b)
print(id(a))
print(id(b))

# 다차원 리스트 복사 방식
import copy
print("-------------copy() 함수 미적용 예시--------------")
c = [[1,2],[3,4,5]]
d = c.copy()  #일차원 복사만 적용 
print(d)
d[0][0] = 0   #
print(c)
print(d)
print(id(c))
print(id(d))
print("---------copy.deepcopy() 함수 적용 예시-----------")
d = copy.deepcopy(c)
print(c)
print(d)
print(id(c))
print(id(d))