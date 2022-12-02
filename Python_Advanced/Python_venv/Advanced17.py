# 스레드와 프로세스 - 동시성과 병렬성
'''
* 프로그램
 - 작업을 수행하는 명령어 집합
* 프로세스
 - 실행중인 프로그램
 - 메모리에 반영되어 있는 살아있는 프로그램
 - 멀티 프로세스 : 프로세스를 여러개를 두고 있음(= 멀티 코어)
   : 프로세스는 실제로 동시에 진행됨 (= 프로세스의 병렬성)
 - 멀티 프로세싱
   : 병렬성 프로그래밍
     실제로 작업이 동시에 일어되는 것
     프로세스를 여러 개 만들어 동시에 실행

* 스레드
 - 프로세스에서 실행되는 작업
 - 프로세스는 기본적으로 하나의 스레드로 구성된다
 - 경우에 따라 여러 개의 스레드로 구성이 가능하다 (= 멀티 스레딩)
 - thread의 동시성
   : 실제로 동시에 진행되는 것은 아니지만 동시에 진행되는 것처럼 스레드가 잘게 쪼개져 나눠 실행됨(멀티 스레딩)
 - 멀티 스레딩
   : 동시성 프로그래밍
     동시에 실행되는 것처럼 보이는 것
     스레드 여러 개를 번갈아 가면서 실행

* 자원의 소모가 큰 것은? 멀티 프로세싱
 - 프로세스를 만드는 것 자체가 고비용! (vs 스레드)

* 파이썬에서 스레드를 관리할 수 있는 모듈
 => threading
   - IO 작업 시 자주 사용된다!

* 파이썬 멀티프로세스 모듈
 => multiprocessing 

 
'''


import threading  # 내장 모듈
import time

'''
# 스레드를 실행할 함수
def work() :
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>> ")
    print(f"[sub] {keyword}로 검색을 시작합니다...")
    print("[sub] end")

# 메인스레드가 실행되는 부분
print("[main] start")

worker = threading.Thread(target=work) 
worker.start()

print("[main] 메인 스레드는 자기 할 일을 합니다..")
print("[main] end")
'''

'''
# 데몬 스레드 - 메인 스레드 종료 시 같이 종료된다

# 스레드를 실행할 함수
def works() :
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>> ")
    print(f"[sub] {keyword}로 검색을 시작합니다...")
    print("[sub] end")

# 메인스레드가 실행되는 부분
print("[main] start")

worker = threading.Thread(target=works) 
worker.daemon = True
worker.start()

print("[main] 메인 스레드는 자기 할 일을 합니다..")
print("[main] end")
'''

'''
# 주식 자동 매매
# 매수, 매도

# 매수 Thread
def buyer() :
    for i in range(5) :
        print("[매수] 데이터 요청 중...")
        time.sleep(1)
        print("[매수] 데이터 분석 중...")
        time.sleep(1)
        print("[매수] 매수 타이밍...")
        time.sleep(1)
        print("[매수] 매수 진행...")
        time.sleep(1)

# 매도 Thread
def saler() :
    for i in range(5) :
        print("[매도] 데이터 요청 중...")
        time.sleep(1)
        print("[매도] 데이터 분석 중...")
        time.sleep(1)
        print("[매도] 매도 타이밍...")
        time.sleep(1)
        print("[매도] 매도 진행...")
        time.sleep(1)

# 메인 스레드
print("[메인] start")
buyer = threading.Thread(target=buyer)
saler = threading.Thread(target=saler)
buyer.start()
saler.start()

buyer.join()  # 매수 스레드가 종료될 때까지 메인 스레드가 기다림
saler.join()  # 매도 스레드가 종료될 때까지 메인 스레드가 기다림
print("[메인] 창이 종료되었습니다.")
'''

# multiprocessing 모듈 사용

import multiprocessing as mp

'''
# 프로세스에서 실행할 함수
def sub_process(name) :
    print("[sub] start")
    print(name)
    cp = mp.current_process()
    print(f"[sub] pid : {cp.pid}")
    print("[sub] end")

# 메인 프로세스
if __name__ == "__main__" : #윈도우 운영체제의 경우 조건을 걸어줘야 한다! (미포함 시 런타임 에러 발생!)
    print("[main] start")
    p = mp.Process(target=sub_process, args=('Python_Study',))
    p.start()
    cp = mp.current_process()
    print(f"[main] pid : {cp.pid}")
    print("[main] end")
'''

'''
# 클래스를 이용한 멀티 프로세싱 활용

from multiprocessing import Process
import time

# 클래스로 서브 프로세스 지정
class Subprocess(Process) :
    def __init__(self,name) :
        Process.__init__(self)
        self.name = name
    
    def run(self) :
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")

if __name__ == "__main__" :
    print("[main] start")
    p = Subprocess(name = 'Python_Study')
    p.start()
    p.join()    # 서브프로세스가 종료될 때까지 기다렸다 종료
    print("[main] end")
'''

# 프로세스가 살아있는지 확인하는 방법(프로세스.is_alive())
from multiprocessing import Process
import time

# 클래스로 서브 프로세스 지정
class Subprocess(Process) :
    def __init__(self,name) :
        Process.__init__(self)
        self.name = name
    
    def run(self) :
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")

if __name__ == "__main__" :
    print("[main] start")
    p = Subprocess(name = 'Python_Study')
    p.start()
    print(p.is_alive()) # 프로세스가 살아있는지 확인
    time.sleep(2)
    if p.is_alive:
        p.terminate()   # 프로세스를 강제 종료하는 방법!
    p.join()    # 서브프로세스가 종료될 때까지 기다렸다 종료
    print("[main] end")
    print(p.is_alive()) # 프로세스가 살아있는지 확인


# 추가 학습
'''
1. 스레드 간 데이터 처리 (lock)
2. 프로세스 간 데이터 전송 (Queue, Pipe)
3. 속도 비교
4. 운영체제와 메모리(스레드간 메모리 공유 방식, 프로세스 간 메모리 공유 방식)
'''