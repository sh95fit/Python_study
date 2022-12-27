# PySide 실습 - 포스기 프로그램
'''
컴퓨터는 CRUD(Create Read Update Delete)를 처리한다!
주문 내역 - READ에 해당
주문 넣기 - CREATE에 해당

보통은 READ 영역을 먼저 구성한 후 CREATE를 구성한다!
READ 영역을 먼저 구현해놓으면 CREATE 작업 시 잘 되고 있는지 판단이 가능하다!
'''


import sys
import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem

from PySide6.QtCore import QTimer

from Qt_Pos import Ui_MainWindow

# 주문 내역에 넣을 dummy 값을 임시로 만들어줌 (주문 내역에 잘 표시가 되는지 확인하기 위한 용도) - CREATE보다 READ를 먼저 구현하기 위한 확인 용도!
# dummy = [
#     {"menu" : "에스프레소 L", "quantity" : "10", "order_amount" : "10000", "time" : "2022-12-27 16:16:00", "status" : "waiting"},
#     {"menu": "에스프레소 L", "quantity": "10", "order_amount": "10000", "time": "2022-12-27 16:16:00", "status": "done"}
# ]

# 실제 주문 내역
orders = [

]

menu_widgets = [
    "radio_espresso",
    "radio_americano",
    "radio_latte",
    "radio_mocha",
    "radio_choco_smoothie",
    "radio_strawberry_smoothie",
]

size_widgets = [
    "radio_size_s",
    "radio_size_m",
    "radio_size_l",
    "radio_size_xl",
]


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 현재 시각 표현을 위한 타이머
        self.timer = QTimer()
        self.timer.setInterval(990)    # 타이머 간격 주기
        self.timer.timeout.connect(self.tick)
        self.timer.start()

        self.load()

        for w in menu_widgets + size_widgets :
            widget = getattr(self.ui, w)
            widget.clicked.connect(self.calc)
        
        # 시작 될때 총 금액이 1회 계산
        self.calc()

    # 현재 시각 
    def tick(self) :
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        self.ui.lb_now.setText(f"현재 시각 : {now}")

    # 주문 내역 불러오기
    # 테이블에 데이터 표시를 위해 QTableWidgetItem 활용
    def load(self) :
        for d in orders :
            r = self.ui.table_orders.rowCount() # 마지막 줄의 기준
            self.ui.table_orders.insertRow(r)   # 마지막 줄에 row 추가
            self.ui.table_orders.setItem(r, 0, QTableWidgetItem(d["menu"]))    # setItem(row, column, item)
            self.ui.table_orders.setItem(r, 1, QTableWidgetItem(d["quantity"]))
            self.ui.table_orders.setItem(r, 2, QTableWidgetItem(d["order_amount"]))
            self.ui.table_orders.setItem(r, 3, QTableWidgetItem(d["time"]))
            self.ui.table_orders.setItem(r, 4, QTableWidgetItem(d["status"]))

        # LCD 주문 현황 업데이트
        self.ui.lcd_num_of_orders.display(len(orders))
        waiting = [x for x in orders if x["status"] == "waiting"]
        self.ui.lcd_num_of_orders_waiting.display(len(waiting))
        processing = [x for x in orders if x["status"] == "processing"]
        self.ui.lcd_num_of_orders_processing.display(len(processing))
        delivery = [x for x in orders if x["status"] == "delivery"]
        self.ui.lcd_num_of_orders_delivery.display(len(delivery))
        done = [x for x in orders if x["status"] == "done"]
        self.ui.lcd_num_of_orders_done.display(len(done))
    
    # 총 주문 금액 계산
    def calc(self) :
        menu_price = {
            "에스프레소" : 2000,
            "아메리카노" : 1500,
            "카페 라떼" : 3000,
            "카페 모카" : 3500,
            "초코 스무디" : 5500,
            "딸기 스무디" : 5500,
        }
        size_price = {
            "S" : 0,
            "M" : 500,
            "L" : 1000,
            "XL" : 1500,
        }

        price = 0

        for w in menu_widgets :
            menu = getattr(self.ui, w)
            if menu.isChecked() :
                price = menu_price[(menu.text())]
                break
        for w in size_widgets :
            size = getattr(self.ui, w)
            if size.isChecked():
                price += size_price[(size.text())]      # 사이즈에 따른 추가금액이므로 음료 가격 price에 더하는 형태
                break

        quantity = self.ui.spin_quantity.value()
        price = price*quantity

        self.ui.lb_order_amount.setText(f"총 주문 금액 : {price}원")
        
        return price


if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())