# PySide 실습 - 메일 뷰어
'''
GUI
성능 이슈가 큰 문제이므로 성능적인 측면 개선을 위해 힘써야한다
변경성이 크므로 유지보수 측면을 중점적으로 검토하여야한다

크롤링 + PySide 접목하여 메일 뷰어 만들어보기
'''

import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from Qt_Mailviewer import Ui_MainWindow

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    


if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show

    sys.exit(app.exec())