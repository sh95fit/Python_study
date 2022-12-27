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

 - 여러 창을 띄우고 서로 소통이 가능하도록 연동
  보통은 서버를 통해 연동하지만 파일을 활용한 연동도 가능하다!

'''

import sys
import random

from PySide6.QtCore import QTimer

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTextBrowser

from Qt_Messenger import Ui_MainWindow

# list Widget이 아닌 list view를 사용하는 경우 모델을 선정해주어야 한다!
# from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow) :
    last_read = 0

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

        # 랜덤 
        # nickname 호출
        nickname = self.random_nickname()
        self.ui.edit_nickname.setText(nickname)

        # 환영합니다 메세지 띄우기(접속 확인)
        with open("./Python_PySide_GUI/Qt_server.txt", "a+", encoding='UTF-8') as f :
            f.writelines(f"---------{nickname}님이 접속하셨습니다.---------\n")

        # 파일 최초 1회 로드
        self.listen()

        # 특정 시간마다 listen() 함수 실행 (입력 시에만 받아오는 것을 수시로 받아오는 것으로 설정하기 위함)
        self.timer = QTimer()
        self.timer.setInterval(100)    # 단위 : ms
        self.timer.timeout.connect(self.listen)
        self.timer.start()

    
    def send(self) :
        nickname = self.ui.edit_nickname.text()

        # list Widget을 사용하는 경우
        text = self.ui.edit_text.text()
        # self.ui.list_chat.addItem(f"{nickname} : {text}")

        # 파일 연동하기
        msg = f"{nickname} : {text}"

        # 파일에 메세지 쓰기
        with open("./Python_PySide_GUI/Qt_server.txt", "a", encoding="UTF-8") as f :
            f.writelines(msg + "\n")

        # 전송 후 클리어 적용
        self.ui.edit_text.clear()

        # 파일 읽어오기
        self.listen()

        # list view를 사용하는 경우!
        # text = self.ui.edit_text.toPlainText()
        # item = QStandardItem(text)      # 모델은 StandardItemModel이므로  text가 아닌 StandardItem을 넣어줘야 한다!
        # self.model.appendRow(item)      # 줄을 추가한 후 위 텍스트를 반영


        # 입력된 값이 전송 버튼에 의해 적용되는지 확인하는 용도!
        # mb = QMessageBox()
        # mb.setText(self.ui.edit_text.toPlainText())   # text edit의 입력은 .toPlainText 활용
        # mb.exec()

    # 랜덤 닉네임 생성
    def random_nickname(self) :
        nickname = random.choice(["홍길동","장보고","이순신"])
        num = random.randint(1, 1000)
        return f"{nickname}{num}"
    
    # 서버 대신 사용하는 파일이 로드된 것을 받기 위함
    def listen(self) :
        try :   # 파일이 없는 경우 발생하는 에러를 처리하기 위해 try-except 구문 활용
            with open("./Python_PySide_GUI/Qt_server.txt", "r", encoding="UTF-8") as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            self.ui.list_chat.addItems(lines[self.last_read:])
            self.last_read = len(lines)
            self.ui.list_chat.scrollToBottom()  # 새로운 라인 추가 후 스크롤을 가장 아래로 내리기 (But, Timer로 지속 실행되므로 이전 리스트 확인이 어려움)
        except :
            pass

if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())