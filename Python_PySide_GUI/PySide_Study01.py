# PySide6 설치
# https://doc.qt.io/qtforpython/quickstart.html
'''
PySide6 설치
pip install pyside6
'''

import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

# PySide6 설치 확인(버전)
# print(PySide6.__version__)
# print(PySide6.QtCore.__version__)

class MyWidget(QtWidgets.QWidget) :
    def __init__(self) :
        super().__init__()

        self.hello = ["김치찌개", "된장찌개", '순두부찌개', '곱창전골']

        self.button = QtWidgets.QPushButton("Click")
        self.text = QtWidgets.QLabel("Choice Food!", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self) :
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())