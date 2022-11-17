# 리스트 관련 메서드, 리스트 내포
'''
리스트에서 유용한 메서드

* 리스트에서 데이터 추가
-> 리스트.append(데이터)

list = [데이터1, 데이터2]
list.append(데이터3)

Tip. 리스트 내 리스트를 추가할 수 있다!

* 리스트에서 데이터 삭제
-> 리스트.pop()    # 괄호 안에 아무것도 넣지 않으면 마지막 데이터 삭제! 인덱스 사용 시 해당 위치 데이터 삭제
-> 리스트.remove()
-> del 리스트[인덱스]

* 리스트 특정 값의 인덱스를 구하는 방법
-> 리스트.index(데이터)

* 리스트 특정 값의 개수를 구하는 방법
-> 리스트.count()

* 리스트의 모든 요소 삭제
-> 리스트.clear()

* 리스트 정렬하기
-> 리스트.sort()  오름차순 정렬
-> 리스트.sort(reverse = True) 역순 정렬

** enumerate
for in 반복문 사용 시 인덱스를 같이 출력하는 방법!
-> for 인덱스, 데이터 in enumerate(리스트) :

ex> for index, number in enumerate(리스트) :
    print(index, number)


# 리스트 내포
for문, if문 등을 지정해 리스트를 간편하게 하는 것
순서  1.for문 -> 2.if문 -> 3.표현식 -> 4.리스트로 만들어 줌


for문 사용
[표현식 for 변수 in 순회가능한 데이터]

ex> nums = [i for i in range(5)]
ex2> nums = [i*2 for i in nums]

if문 사용
[표현식 for문 if 조건]

ex> nums = [i for i in range(10) if i%2 == 0]
'''

# 리스트 메서드

# 리스트 데이터 삭제
list = ['데이터1', '데이터4', '데이터2', '데이터3', '데이터0']
list.pop(1)
print(list)

# 리스트 정렬
list.sort()
print(list)

# enumerate
for index, data in enumerate(list) :
    print(index+1, data)
    print(f"{index+1}번째 데이터는 {data}입니다.")


# 리스트 내포

#for문 사용
nums  = [i for i in range(5)]
print(nums)

nums2 = [100,200,300]
double_nums = [i*2 for i in nums2]
print(double_nums)

#if문 사용
nums3 = [i for i in range(10) if i%2 == 0]
print(nums3)

nums4 = [100, 200, 300, 400, 500]
double_nums4 = [i*2 for i in nums4 if i>= 300]
print(double_nums4)