# Tutle 라이브러리
'''
그래픽 출력 지원 라이브러리

shape : 모양 - arrow(화살표), turtle(거북이), square(사각형), circle(원), triangle(삼각형)
fillcolor(색상이름)
color(색상이름)
pensize(숫자) - 펜의 굵기
speed(숫자) - 속도
circle(숫자) - 반지름
'''

import turtle

t = turtle.Turtle()

t.shape("turtle")
t.forward(100)  #이동 - 초기 방향 좌->우
t.right(90)  #회전
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

print("사각형 출력하기")

# 삼각형
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

print("삼각형 출력하기")

t.shape("arrow")
t.color("red")
t.pensize(3)
t.circle(100)

print("원 출력하기")


colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
turtle.bgcolor('black')   #배경색
t.speed(0)
t.width(3)  #펜의 굵기 3
length = 10
while length < 500 :
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5

print("사이즈, 컬러가 다른 사각형 증대 출력하기")

t.shape("turtle")
t.color('red')
t.pensize(5)

for i in range(5):
    t.forward(200)
    t.left(144)

print("별 출력하기")


t.shape("turtle")
t.color('blue')
t.speed(0)
t.pensize(3)

n = 50
for i in range(n):
    t.circle(100)
    t.left(360/n)

print("원 이동 출력하기")


t.shape("turtle")
t.color('purple')
t.speed(0)
t.pensize(1)

for i in range(200):
    t.forward(i)
    t.left(89)
t.hideturtle()


t.shape("turtle")
t.color('green')
t.speed(0)
t.pensize(1)

for i in range(5*3) :
    t.forward(300+i*10)
    t.left(360/5*2)


t.shape("turtle")

for i in range(5) :
    t.forward(100)
    t.left(360/5)
    
print("오각형 그리기")


for i in range(50) :
    t.forward(100)
    t.left(360/6)
    t.left(10)


t.shape('square')
t.width(3)

for i in range(1,200,5):
    t.forward(i)
    t.left(90)