# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Qt_Pos.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QGroupBox, QHeaderView,
    QLCDNumber, QLabel, QMainWindow, QPushButton,
    QRadioButton, QScrollBar, QSizePolicy, QSlider,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(790, 460)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lb_now = QLabel(self.centralwidget)
        self.lb_now.setObjectName(u"lb_now")
        self.lb_now.setGeometry(QRect(10, 10, 261, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lb_now.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 81, 21))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lcd_num_of_orders = QLCDNumber(self.centralwidget)
        self.lcd_num_of_orders.setObjectName(u"lcd_num_of_orders")
        self.lcd_num_of_orders.setGeometry(QRect(90, 75, 71, 31))
        self.lcd_num_of_orders_waiting = QLCDNumber(self.centralwidget)
        self.lcd_num_of_orders_waiting.setObjectName(u"lcd_num_of_orders_waiting")
        self.lcd_num_of_orders_waiting.setGeometry(QRect(90, 115, 71, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 81, 21))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lcd_num_of_orders_processing = QLCDNumber(self.centralwidget)
        self.lcd_num_of_orders_processing.setObjectName(u"lcd_num_of_orders_processing")
        self.lcd_num_of_orders_processing.setGeometry(QRect(90, 155, 71, 31))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 81, 21))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.lcd_num_of_orders_delivery = QLCDNumber(self.centralwidget)
        self.lcd_num_of_orders_delivery.setObjectName(u"lcd_num_of_orders_delivery")
        self.lcd_num_of_orders_delivery.setGeometry(QRect(90, 195, 71, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 200, 81, 21))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.lcd_num_of_orders_done = QLCDNumber(self.centralwidget)
        self.lcd_num_of_orders_done.setObjectName(u"lcd_num_of_orders_done")
        self.lcd_num_of_orders_done.setGeometry(QRect(90, 235, 71, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 240, 81, 21))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(170, 50, 601, 391))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.table_orders = QTableWidget(self.tab)
        if (self.table_orders.columnCount() < 5):
            self.table_orders.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_orders.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_orders.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_orders.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_orders.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_orders.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_orders.setObjectName(u"table_orders")
        self.table_orders.setGeometry(QRect(0, 0, 591, 361))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 111, 211))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.radio_espresso = QRadioButton(self.groupBox)
        self.radio_espresso.setObjectName(u"radio_espresso")
        self.radio_espresso.setGeometry(QRect(10, 30, 101, 20))
        self.radio_espresso.setChecked(True)
        self.radio_americano = QRadioButton(self.groupBox)
        self.radio_americano.setObjectName(u"radio_americano")
        self.radio_americano.setGeometry(QRect(10, 60, 101, 20))
        self.radio_latte = QRadioButton(self.groupBox)
        self.radio_latte.setObjectName(u"radio_latte")
        self.radio_latte.setGeometry(QRect(10, 90, 101, 20))
        self.radio_mocha = QRadioButton(self.groupBox)
        self.radio_mocha.setObjectName(u"radio_mocha")
        self.radio_mocha.setGeometry(QRect(10, 120, 101, 20))
        self.radio_choco_smoothie = QRadioButton(self.groupBox)
        self.radio_choco_smoothie.setObjectName(u"radio_choco_smoothie")
        self.radio_choco_smoothie.setGeometry(QRect(10, 150, 101, 20))
        self.radio_strawberry_smoothie = QRadioButton(self.groupBox)
        self.radio_strawberry_smoothie.setObjectName(u"radio_strawberry_smoothie")
        self.radio_strawberry_smoothie.setGeometry(QRect(10, 180, 101, 20))
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(130, 10, 101, 211))
        self.groupBox_2.setFont(font1)
        self.radio_size_m = QRadioButton(self.groupBox_2)
        self.radio_size_m.setObjectName(u"radio_size_m")
        self.radio_size_m.setGeometry(QRect(10, 80, 91, 20))
        self.radio_size_s = QRadioButton(self.groupBox_2)
        self.radio_size_s.setObjectName(u"radio_size_s")
        self.radio_size_s.setGeometry(QRect(10, 30, 91, 20))
        self.radio_size_s.setChecked(True)
        self.radio_size_l = QRadioButton(self.groupBox_2)
        self.radio_size_l.setObjectName(u"radio_size_l")
        self.radio_size_l.setGeometry(QRect(10, 130, 91, 20))
        self.radio_size_xl = QRadioButton(self.groupBox_2)
        self.radio_size_xl.setObjectName(u"radio_size_xl")
        self.radio_size_xl.setGeometry(QRect(10, 180, 91, 20))
        self.groupBox_3 = QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(240, 10, 341, 211))
        self.groupBox_3.setFont(font1)
        self.spin_quantity = QSpinBox(self.groupBox_3)
        self.spin_quantity.setObjectName(u"spin_quantity")
        self.spin_quantity.setGeometry(QRect(10, 30, 121, 21))
        self.spin_quantity.setLayoutDirection(Qt.LeftToRight)
        self.spin_quantity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spin_quantity.setMinimum(1)
        self.hs_quantity = QSlider(self.groupBox_3)
        self.hs_quantity.setObjectName(u"hs_quantity")
        self.hs_quantity.setGeometry(QRect(10, 70, 271, 22))
        self.hs_quantity.setMinimum(1)
        self.hs_quantity.setOrientation(Qt.Horizontal)
        self.vs_quantity = QScrollBar(self.groupBox_3)
        self.vs_quantity.setObjectName(u"vs_quantity")
        self.vs_quantity.setGeometry(QRect(310, 20, 16, 181))
        self.vs_quantity.setMinimum(1)
        self.vs_quantity.setOrientation(Qt.Vertical)
        self.dial_quantity = QDial(self.groupBox_3)
        self.dial_quantity.setObjectName(u"dial_quantity")
        self.dial_quantity.setGeometry(QRect(100, 100, 111, 91))
        self.dial_quantity.setMinimum(1)
        self.lb_order_amount = QLabel(self.tab_2)
        self.lb_order_amount.setObjectName(u"lb_order_amount")
        self.lb_order_amount.setGeometry(QRect(80, 230, 421, 61))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.lb_order_amount.setFont(font2)
        self.btn_order = QPushButton(self.tab_2)
        self.btn_order.setObjectName(u"btn_order")
        self.btn_order.setGeometry(QRect(30, 300, 531, 51))
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_now.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \uc2dc\uac01 : ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc624\ub298 \uc8fc\ubb38 ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\ub300\uae30 \uc911", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ucc98\ub9ac \uc911", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uc1a1 \uc911", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc", None))
        ___qtablewidgetitem = self.table_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274", None));
        ___qtablewidgetitem1 = self.table_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uc218\ub7c9", None));
        ___qtablewidgetitem2 = self.table_orders.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38 \uae08\uc561", None));
        ___qtablewidgetitem3 = self.table_orders.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38 \uc2dc\uac01", None));
        ___qtablewidgetitem4 = self.table_orders.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\ud0dc", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38 \ub0b4\uc5ed", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\uba54\ub274", None))
        self.radio_espresso.setText(QCoreApplication.translate("MainWindow", u"\uc5d0\uc2a4\ud504\ub808\uc18c", None))
        self.radio_americano.setText(QCoreApplication.translate("MainWindow", u"\uc544\uba54\ub9ac\uce74\ub178", None))
        self.radio_latte.setText(QCoreApplication.translate("MainWindow", u"\uce74\ud398 \ub77c\ub5bc", None))
        self.radio_mocha.setText(QCoreApplication.translate("MainWindow", u"\uce74\ud398 \ubaa8\uce74", None))
        self.radio_choco_smoothie.setText(QCoreApplication.translate("MainWindow", u"\ucd08\ucf54 \uc2a4\ubb34\ub514", None))
        self.radio_strawberry_smoothie.setText(QCoreApplication.translate("MainWindow", u"\ub538\uae30 \uc2a4\ubb34\ub514", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\uc0ac\uc774\uc988", None))
        self.radio_size_m.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.radio_size_s.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.radio_size_l.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.radio_size_xl.setText(QCoreApplication.translate("MainWindow", u"XL", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\uc218\ub7c9", None))
        self.lb_order_amount.setText(QCoreApplication.translate("MainWindow", u"\ucd1d \uc8fc\ubb38 \uae08\uc561 : ", None))
        self.btn_order.setText(QCoreApplication.translate("MainWindow", u"\ubc1c\uc8fc", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38 \ub123\uae30", None))
    # retranslateUi

