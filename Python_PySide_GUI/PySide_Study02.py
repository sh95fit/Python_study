# PySide6
'''
# TUI, GUI
TUI : Text-based User Interface
GUI : Graphic User interface

# Cross Platform GUI - Qt
- 맥, 윈도우, 리눅스 상관없이 동일한 GUI를 띄우는 기술!
- 주요 특징
 완벽한 GUI 추상화(소스를 짜면 운영체제에 맞춰 Qt 라이브러리가 호환이 되도록 맞춰줌)
 자체 렌더링 엔진
 다양한 언어 지원

# 파이썬용 Qt 라이브러리
 - QtCore
 - QtGui
 - QtWidgets

# Qt 라이선스
 - 오픈소스SW 라이선스 종합정보 시스템(olis.kr)에서 확인
 - Qt의 경우 특정 모듈을 제외하면 LGPS, 소스코드 공개 의무 없음!
  Qt Charts, Qt Data Visualization, Qt Lottie Animation, Qt Network Authorization과 같은 경우 사용함과 동시에 소스코드 공개 필요

# PySide6 Designer
 - GUI 편집기
 - 다운로드 링크
  https://build-system.fman.io/qt-designer-download
 - PySide는 Qt와 호환될 수 있도록 해주는 인터페이스(Qt를 Python에서 사용할 수 있도록 포팅)
 - PySide 설치 위치 확인 필요(PySide 위치에 Qt와 Designer가 설치되므로!)
  Tip! PySide는 Python의 라이브러리이므로 Python 폴더 위치를 찾으면 수월하다!
  cmd 내에서 where python 을 타이핑 하여 위치 찾기 + 경로 드래그 및 우클릭(복사) + 파일 탐색기에 붙여넣기
  Lib 폴더 내 site-packages 폴더 내에 PySide가 설치되어 있음
  -> Designer와 uic.exe(컴파일러와 유사한 역할) 2가지를 찾으면 된다!

 - Qt Designer
  첫 시작 시 Modal 창을 통해 폼 선정
  Ctrl + R 을 통해 실제 폼의 실행상태를 볼 수 있음
  uic를 활용해 ui 내용을 Python 코드로 컴파일!

  uic 실행 방법
  - cmd창에서 .ui 파일이 있는 폴더로 이동 or 터미널 창에서 해당 폴더로 이동
  - uic가 있는 경로 복사 + 경로 뒤 uic를 입력하여 uic 실행!

  간단하게 uic를 실행하는 방법 - Path 환경변수 설정!
  주의 사항! path 설정 후 vs code를 껐다 켜야한다!

 - ui 파일이 있는 폴더로 이동 후 uic 실행
  ex> uic QtDesigner_test.ui > QtDesigner_ui.py
     > : .ui를 변환한 것을 우측 .py 파일로 덮어쓰기해서 생성됨!
 - Qt의 기본은 C++이므로 Python으로 변환하려면 아래와 같이 실행해야 한다!
   uic -g python QtDesigner_test.ui > QtDesigner_ui.py
'''

from PySide6.QtWidgets import QMainWindow, QApplication
from QtDesigner_ui import Ui_MainWindow

import sys

class MainWindow(QMainWindow) :
  def __init__(self) :
    super(MainWindow, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

if __name__ == "__main__" :
  app = QApplication()

  window = MainWindow()
  window.show()

  sys.exit(app.exec())