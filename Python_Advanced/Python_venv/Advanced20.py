# 이터레이터
'''
* 이터러블 객체(iterable object)란 무엇일까?
 - 순서가 있는 자료형   ex> for i in (iterable object) :
 - 문자열, 리스트, 튜플, 딕셔너리, range 객체

# 이터레이터 생성 방법
 - __iter__, __next__ 메서드를 정의해준다. 
'''

# 1. 이터러블 객체(iterable object)
# 문자열, 리스트, 튜플, 딕셔너리, range 객체

# ex
# for i in "123" :
#     print(i)

# 리스트를 이용한 이터러블 객체 동작 원리 확인하기
print(dir([10, 20, 30]))
print(type([10,20,30].__iter__))    # method-wrapper

iter_obj = [10,20,30].__iter__()
#print(iter_obj)
print(dir(iter_obj))

print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())

# 범위를 넘어가면 StopIteration과 함께 에러 발생
# __iter__()를 이용해 이터러블 객체를 만들고 __next__()를 활용해 하나씩 출력한다


# 이터레이터 생성 방법

class Seasons :
    def __init__(self) :
        self.season_list = ['spring', 'summer', 'autumn', 'winter']
        self.idx = 0
        self.max_num = 4
    
    def __iter__(self) :
        return self

    def __next__(self) :
        if self.idx < self.max_num :
            curr_idx = self.idx
            self.idx += 1
            return self.season_list[curr_idx]
        else :
            raise StopIteration


#for i in Seasons() :
#    print(i)

iter_obj = Seasons().__iter__()
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())