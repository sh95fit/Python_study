# 모듈
'''
모듈을 사용하는 이유
프로그램을 기능별로 파일을 나누어주는 역할
-> 유지보수 등 관리를 편하게 하기 위해 사용

모듈이란?
- 1개의 완성된 프로그램 파일

모듈을 사용하는 방법
import 모듈이름
모듈이름.변수
모듈이름.함수()

from 모듈이름 import 변수 or 메서드, ...

파이썬 외부 모듈 사용방법
pip install 모듈이름

Tip. __pycache__ 는 컴파일 속도 향상을 위해 생성되는 캐시 파일
'''

#내장 모듈 - 파이썬 설치 시 자동 설치되는 모듈
import math
print(math.pi)
print(math.ceil(2.7))

# 모듈 이름이 길어서 변수, 함수 앞에 일일이 붙여서 쓰기 번거로운 경우
from math import pi, ceil
print(pi)
print(ceil(2.7))

#변수, 함수 명칭이 길거나 사용하기 불편해 변경해서 사용하고 싶은 경우
#from math import pi, ceil as c
#print(pi)
#print(c(2.7))


#외부 모듈 - 다른 사람이 만든 파이썬 파일을 pip로 설치해서 사용
# 외부 모듈 예 : pyautogui  (매크로 모듈 : 마우스, 키보드를 자동으로 움직이게 만들어줌)
'''
import pyautogui as pg

pg.moveTo(500, 500, duration=2, tween=pg.easeInOutQuad)
'''


#직접 만든 모듈 활용
'''
root 폴더가 아닌 경우 오류메세지가 발생함!
조치 방법(모듈 사용 경로 추가 설정)
파일(File) -> 기본 설정(Preferences) -> 설정(Settings) -> 파일 추가(settings.json)
-> 추가 "python.analysis.extraPaths" : ["./하위폴더/하위폴더.../해당폴더"],
'''
import test_module

#변수 사용
print(test_module.version)

test_module.printAuthor()

#클래스 사용
test_info = test_module.Pay("A102030", 20000, "2021-06-13")
print(test_info.get_pay_info())

#다른 파일에서 실행되므로 __main__이 아닌 모듈명 출력
print(test_module.__name__)