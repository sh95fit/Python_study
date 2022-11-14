# 파일 입출력 - 출력 기초

f = open("test.txt", "r")

while True :
    line = f.readline()
    if not line : break
    print(line, end='')
print("")
f.close()

f = open("test.txt", "r")
lines = f.readlines()  # 한줄씩 리스트에 담기 list =[문장1, 문장2, 문장3 ...]
for line in lines : 
    print(line, end='')
print("")
f.close()

f = open("test.txt", 'r')
data = f.read()
print(data)
f.close


# 파일 f = open("파일명", "열기모드")   // 필수조건 f.close()
'''
with문   
파일 출력 시 close를 생략해도 된다

ex>
with open("test.txt", 'a') as f :
    f.write("글자를 추가합니다.")

'''

with open("test.txt", 'a') as f:
    f.write("글자를 추가합니다.")


# 파일 입출력 실습 - 함수 활용
'''
####################################
#         성적처리프로그램         #
####################################
1. 입력    |  2. 출력  |    3. 종료
'''

def add() :
    f = open("score.txt", "a", encoding = 'utf-8')
    name = input("이름 : ")
    kor = int(input("국어 : "))
    eng = int(input("영어 : "))
    math = int(input("수학 : "))

    sum = kor + eng + math
    avg = sum/3
    f.write("%s   %3d   %3d   %3d   %3d   %.2f\n"%(name, kor, eng, math, sum, avg))
    f.close

def show() :
    f = open("score.txt", "r", encoding="utf-8")
    data = f.read()
    print(data)
    f.close()


print("####################################")
print("#         성적처리프로그램         #")
print("####################################")

while True :
    print("1. 입력    |  2. 출력  |    3. 종료")
    select = int(input("실행할 항목을 선택하세요 >>> "))

    if select == 1 :
        add()
    elif select == 2 :
        show()
    elif select == 3 :
        break


