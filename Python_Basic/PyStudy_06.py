#반복문 - for문, while문
'''
반복적인 작업의 코드로 작성하기 위해 사용

시퀀스 자료형
순서가 있는 자료형
종류 : 리스트, 문자열, range 객체, 튜플, 딕셔너리

for 변수 in 시퀀스 자료 :
    명령문

range 명령어
range(숫자) / 0~(숫자-1)까지의 범위 데이터를 만들어줌
range(시작, 끝+1, 단계)  / 단계는 생략하면 +1


# while문 - 반복할 횟수가 정해지지 않은 경우 사용!
초기식
while 조건식 :       / False가 되면 while 루프를 빠져나온다!
    반복할 명령
    증감식

ex>
i = 0 / 초기식
while i < 10 :
    print(i, "번째")
    i += 1

# 무한 루프
while True :
    반복할 명령
    if 조건식 :
        break    / break를 만나면 while 루프를 빠져나온다!

* continue는 continue 아래 코드를 실행하지 않고 다시 루프의 처음으로 돌아가 루프 실행

'''

'''
for a in [1,2,3,4] :
    print(a)

# for문 - 리스트 사용
champions = ["티모", "이즈리얼", "리신"]

for champion in champions : 
    print("선택할 챔피언은", champion, "입니다.")

# for문 - 문자열 사용
message = "자신감을 가지자!"

for word in message :
    print(word)


# for문 - range 사용
for i in range(1,10):
    print(i)
'''

# while문
i = 0 # 초기식
while i < 10 : # 조건식
    print(i, "번째")
    i += 2 #증감식

# 무한루프
while True : 
    x = input("종료하려면 exit를 입력하세요 >>> ")
    if x == 'exit' :
        break