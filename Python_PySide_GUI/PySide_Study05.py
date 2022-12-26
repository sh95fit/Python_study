# PySide 활용 - 메신저 프로그램
'''
- MVC 기법 == MVVM
 Model, View, Controller
 Model이 변형되면 알아서 아이템을 가져온다
 ex> appendRow를 적용하면 줄을 추가하여 모델을 변형하므로 아이템을 가져와 리스트에 적용 시키는 것
 즉, 무엇이든 적용할 때 모델만 수정을 하면 알아서 반영이 된다!

- list view vs list widget
 list view : 모델이 없음. 직접 만들어줘야 한다
 list widget : 모델을 가지고 있음
'''

import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTextBrowser

from Qt_Messenger import Ui_MainWindow

# list Widget이 아닌 list view를 사용하는 경우 모델을 선정해주어야 한다!
# from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # list view의 모델을 만들어주기 위함!
        # self.model = QStandardItemModel()
        # self.ui.list_chat.setModel(self.model)

        # 전송 버튼 처리
        self.ui.btn_send.clicked.connect(self.send)
        # 엔터 시 메세지 처리
        self.ui.edit_text.returnPressed.connect(self.send)
    
    def send(self) :
        nickname = self.ui.edit_nickname.text()

        # list Widget을 사용하는 경우
        text = self.ui.edit_text.text()
        self.ui.list_chat.addItem(f"{nickname} : {text}")

        # 전송 후 클리어 적용
        self.ui.edit_text.clear()

        # list view를 사용하는 경우!
        # text = self.ui.edit_text.toPlainText()
        # item = QStandardItem(text)      # 모델은 StandardItemModel이므로  text가 아닌 StandardItem을 넣어줘야 한다!
        # self.model.appendRow(item)      # 줄을 추가한 후 위 텍스트를 반영


        # 입력된 값이 전송 버튼에 의해 적용되는지 확인하는 용도!
        # mb = QMessageBox()
        # mb.setText(self.ui.edit_text.toPlainText())   # text edit의 입력은 .toPlainText 활용
        # mb.exec()

if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())