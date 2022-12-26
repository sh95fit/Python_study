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

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from Qt_Design_01 import Ui_btn_Click
import sys

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_btn_Click()
        self.ui.setupUi(self)
    
        self.ui.pushButton.clicked.connect(self.click)  # ()를 통해 함수를 호출하게 되면 버튼이 누르기 전에 호출되어버림! 클릭되었을 때 click 함수 실행을 위해 () 생략!  

    def click(self) :
        # self.ui.pushButton.setText("Click")
        # print("Click")
        mb_text = QMessageBox()
        mb_text.setText("간단한 수학 문제!")
        mb_text.exec()  # exec는 반환값이 int이다 / 사용자가 무엇을 클릭했는지 알려주는 역할
        
        mb_quiz = QMessageBox()
        mb_quiz.setText("1+1 = ?")
        # Role에 따라 버튼의 위치가 달라진다! 
        # ActionRole로 모든 버튼을 생성하면 우리가 원하는 배치가 가능하다(코드 순서대로 생성됨!)
        # mb_quiz.addButton("action role", QMessageBox.ActionRole)
        # mb_quiz.addButton("No role", QMessageBox.NoRole)    
        btn_answer_2 = mb_quiz.addButton("2", QMessageBox.ActionRole)  # 첫번째 버튼 클릭시 결과값 0  몇번 버튼이 출력되는지 확인기 가능하다!
        btn_answer_3 = mb_quiz.addButton("3", QMessageBox.ActionRole)  # 두번째 버튼 클릭시 결과값 1
        # 버튼 순서를 확인하고 싶은 경우
        # res = mb_quiz.exec()
        # print(res)

        mb_quiz.exec()

        if mb_quiz.clickedButton() == btn_answer_2 :
            mb_success = QMessageBox()
            mb_success.setText("정답")
            mb_success.exec()
        elif mb_quiz.clickedButton() == btn_answer_3 :
            mb_fail = QMessageBox()
            mb_fail.setText("오답")
            mb_fail.exec()

if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())  # QApplication을 사용자가 끌 때까지 유효하게 가지고 있다가 사용자가 끄면 파이썬도 같이 종료되도록 하는 소스
