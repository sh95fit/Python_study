# Random 라이브러리 활용
'''
숫자 맞추기 게임
'''

import random #랜덤 라이브러리

randomNumber = random.randint(1,100)
count = 1
while True : 
    try : 
        num = int(input("1~100 사이의 숫자를 입력하세요 >>> "))
        if num > 100 or num <= 0 : 
            print("1~100 사이의 숫자만 입력이 가능합니다!")
        elif num > randomNumber :
            print("DOWN")
        elif num < randomNumber :
            print("UP")
        elif num == randomNumber :
            print("{}회 만에 성공하였습니다.".format(count))
            break
        count += 1
    except :
        print("숫자를 입력하세요!")