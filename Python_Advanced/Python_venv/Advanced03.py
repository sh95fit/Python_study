# 문자열 포맷팅
'''
문자열을 편리하게 만들기 위해 사용

2가지 방법
1. format 메서드
 '{인덱스}'.format(데이터)  

ex> 값이 여러개인 경우
  '{0}, {1}, {2}'.format(데이터1, 데이터2, 데이터3)

* 인덱스를 생략헤도 순차적으로 대입된다!
  순서 지정이 필요한 경우 인덱스 사용

2. f-string
  변수1
  변수2
  변수3
  msg = f'{변수1} {변수2} {변수3}'
 

ex> 
문자열 포맷팅이 없는 경우
-> 홍길동님 수강기간이 7일 남았습니다. 문자열 출력
name = "홍길동"
duration = 7
message = name + "님 수강기간이 " + str(duration) + "일 남았습니다."
print(message)

문자열 포맷팅 사용 시! (자료형 변환 불필요)
message_format = f"{name}님 수강기간이 {duration}일 남았습니다."
'''


# format 메서드 사용
print('Hello {} {} {}'.format('apple', 'pineapple', 'pen'))
print('Hello {2} {0} {1}'.format('apple', 'pineapple', 'pen'))

# f-string
name1 = 'apple'
name2 = 'pineapple'
name3 = 'pen'
print(f"Hello {name1} {name2} {name3}")