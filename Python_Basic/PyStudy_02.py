'''
While 조건식
    문장
'''

a = 5
while a > 0 :
    print(a)
    a -= 1

b = 5  # 숫자가 0이 되면 False가 되므로 while 루프를 벗어남
while b :
    print(b)
    b -= 1


# 커피 판매

try :
    sum = int(input("판매할 커피 수는 ? "))

    while True :
        a = int(input("판매할 커피 수 : "))
        sum = sum - a
        if sum <= 0 : 
            print("판매 완료")
            break

except :
    print("숫자를 입력하세요")


# 포맷팅
a = 5
b = 10
c = 7
d = 3

print("a = ", a, "b = ", b)
print("a = %d, b = %d"%(a, b))
print(f'a = {a} b = {b}')


s = 'a = {0} b = {1}'.format(a, b)   #순서대로 인덱스 할당
print(s)

s = 'a = {0:02d} b = {1:3d} c = {2:04d} d = {3:5d}'.format(a, b, c ,d)
print(s)
