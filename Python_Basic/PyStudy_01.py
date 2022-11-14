#예외처리

try :
    a = int(input("숫자를 입력하세요"))
    print("입력된 숫자 : %d"%a)
except:
    print("숫자를 입력하세요!")

'''
for문
for 변수 in 리스트
    수행문장1
    수행문장2
'''

list1 = [1,2,3,4,5,6,7]
for i in list1 :
    print(i)

n = 0
list2 = [1,2,3,4,5,6,7,8,9]
for i in list2 :
    n += 1
    if i%2 : continue
    print(i)

list3 = [91, 40, 88, 55, 71]

for i in list3 :
    if i >= 80 :
        print("합격입니다.")
    else :
        print("불합격입니다.")

'''
for 변수 in range(시작, 종료[, 스텝]) :
    수행문장
'''

for i in range(1,11) :
    print(i)


sum = 0
for i in range(1,11) :
    sum = sum + i
print(sum)


'''
for문 중첩 가능
ex>
  for 변수1 in range(1,10) :
    for 변수2 in rnage(1,10) :
        수행문장
'''
#구구단 출력
for i in range(2,10) :
    for j in range(1,10) :
        print("%d * %d = %2d"%(i,j,i*j))
    print("----------")

# 가로 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print("%d * %d = %2d" % (i, j, i*j), end=' ')
    print()


# 세로 구구단
for i in range(1,10) :
    for j in range(2,10) :
        print("%d * %d = %2d"%(j, i, i*j), end = ' ')
    print()


# 삼각형
'''
*
**
***
****
*****
'''

for i in range(1,6) :
    for j in range(i) :
        print("*", end = '')
    print()


# 역삼각형
'''
*****
****
***
**
*
'''

for i in range(5,0, -1) :
    for j in range(i) :
        print("*", end = '')
    print()


# 삼각형 반전
'''
    *
   **
  ***
 ****
*****
'''

for i in range(1,6) :
    for j in range(5-i, 0, -1) :
        print(end = ' ')
    for k in range(i) :
        print('*', end='')
    print()

# 역삼각형 반전
'''
*****
 ****
  ***
   **
    *
'''

for i in range(5, 0, -1) :
    for j in range(5-i, 0, -1) :
        print(end = ' ')
    for k in range(i) :
        print('*', end='')
    print()


# 피라미드
'''
     *
    ***
   *****
  *******
 *********
'''

for i in range(1, 6) : 
    for j in range(5-i, 0, -1) :
        print(end=' ')
    for k in range(i*2-1) :
        print('*', end='')
    print()


# 역피라미드
'''
 *********
  *******
   *****
    ***
     *
'''

for i in range(5, 0, -1) : 
    for j in range(5-i) :
        print(end = ' ')
    for k in range(i * 2 - 1) :
        print('*', end='')
    print()


# 마름모
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

for i in range(1, 7):
    for j in range(6-i, 0, -1):
        print(end=' ')
    for k in range(i*2-1):
        print('*', end='')
    print()
for i in range(5, 0, -1):
    for j in range(6-i):
        print(end=' ')
    for k in range(i * 2 - 1):
        print('*', end='')
    print()


# 루프 제어문
'''
1. break : 반복문을 빠져나온다.
2. continue : continue 아래 문장을 실행하지 않고 반복문을 계속 진행한다.
'''

for i in range(1, 1001) :
    if i == 701 : break
    print(i)

for j in range(1, 1001) :
    if j % 10 : continue
    print(j)

b = True
for i in range(1, 1001) :
    for j in range(1, 1001) :
        print(j)
        if(j == 500) :
            b = False
            break
    if b == False : break