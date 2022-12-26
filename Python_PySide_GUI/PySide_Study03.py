# PySide Widgets 활용
'''
Layout
다른 위젯들의 구도를 잡아주는 역할
Horizontal layout : 가로 배치
Vertical layout : 세로 배치
Grid layout : 격자로 나눠 widget들이 차지하는 범위를 잡아 격자 내 위치를 구성하는 것
Form layout : 양식이 정해져 있음(요수에 맞춰 폼이 맞춰지는 것)
'''

# PySide 활용 - button + 팝업창 테스트
'''
Signal(요청 - Clicked 이벤트) -> Slot(응답(반환) - Slot Activate)
Slot이 우선 등록되어 있어야 Signal이 발생했을 때 Slot을 수행한다!
'''

from PySide6.QtWidgets import QMainWindow, QApplication
from Qt_Design_01 import Ui_btn_Click
import sys

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_btn_Click()
        self.ui.setupUi(self)
    
        self.ui.pushButton.clicked.connect(self.click)  # ()를 통해 함수를 호출하게 되면 버튼이 누르기 전에 호출되어버림! 클릭되었을 때 click 함수 실행을 위해 () 생략!  

    def click(self) :
        self.ui.pushButton.setText("Click")
        print("Click")

if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())  # QApplication을 사용자가 끌 때까지 유효하게 가지고 있다가 사용자가 끄면 파이썬도 같이 종료되도록 하는 소스
