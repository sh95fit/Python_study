# 예외처리
'''
예외처리가 필요한 이유
프로그램 실행 중 발생하는 에러를 미연에 방지하기 위함

프로그램 사용자가 개발자 의도대로만 사용하지 않을 것
ex> 숫자를 입려하라고 하였으나 문자, 공백 등을 입력하는 경우 등
의도치 않은 경우 발생 시 프로그램이 제대로 처리 못하고 에러가 발생
-> 프로그램이 오류가 발생하면서 죽게 되는 경우 발생!


try-except 구문
try : 
    예외가 발생할 수 있는 코드
except : 
    예외 발생 시 실행할 코드


else, finally
else :
    예외가 발생하지 않은 경우 실행하는 코드
finally :
    항상 실행할 코드 (예외 발생해도 리소스를 반환하도록 하는 경우 사용)    


에러를 강제로 발생시키는 방법!

raise 구문 사용법
raise 예외("에러메세지")
ex>
raise Exception
raise Exception("에러 메세지")


예외 계층 구조
ex>
+--Exception
    +--ArithmeticError
        +--FloatingPointError
        +--OverfileError
        +--ZeroDivisionError
예외 계층 구조에서
상위 에러를 except에 반영하면 하위 에러 모두를 포함할 수 있다
ex> except ArithmeticError : 
    -> FloatingPointError, OverFileError, ZeroDivisionError
특정 에러만 지칭하고 싶은 경우 하위 에러 명시
ex> except ZeroDivisionError :

모든 내장된 예외를 받고 싶은 경우 Exception 사용
ex> except Exception :


에러 만들기
class 예외이름(Exception) :
    def __init__(self) :
        super().__init__("에러메세지")



'''

# 원화, 환율 입력 -> 달러 값을 출력
won = input("원화금액을 입력하세요 >>> ")
dollar = input("환율을 입력하세요 >>> ")

# int 변환 내 문자를 쓰는 경우, 나누기 분모에 0이 되는 경우 에러 발생 
try : #예외가 발생할 수 있는 코드 (예외가 발생해도 프로그램을 종료시키지 않음)
    print(int(won)/int(dollar))
except ValueError as ev : #특정 에러에 대해서 명시하여 예외처리 가능
    print("문자열 입력에 따른 예외 발생", ev)
except ZeroDivisionError as ez :
    print("분모 0 입력 예외가 발생하였습니다.", ez)
except : #예외가 발생했을 때 실행되는 코드
    print("예외가 발생했습니다.")
else : 
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally : #파일을 열고 나서 반드시 닫아줘야하는 등 리소스를 반드시 반환해줘야 하는 경우 사용
    print("예외 발생 유무와 무관하게 항상 실행")


# raise 구문 사용 - 에러 강제 발생
try :
    num = int(input("음수를 입력해 주세요 >>> "))
    if num >= 0 :
        raise Exception("양수는 입력 불가")    # Exception 부분은 상세 예외로 변경 가능
except Exception as e :
    print("에러 발생 : ", e)

# 에러 만들기
class PositiveNumberError(Exception) :
    def __init__(self) :
        super().__init__("양수는 입력 불가")

try:
    num = int(input("음수를 입력해 주세요 >>> "))
    if num >= 0:
        raise PositiveNumberError    # Exception 부분은 상세 예외로 변경 가능
except PositiveNumberError as e:
    print("에러 발생 : ", e)