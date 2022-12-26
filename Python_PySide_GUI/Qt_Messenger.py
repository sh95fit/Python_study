# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Qt_Messenger.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(382, 513)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.list_chat = QListWidget(self.centralwidget)
        self.list_chat.setObjectName(u"list_chat")
        self.list_chat.setGeometry(QRect(10, 10, 361, 411))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 430, 81, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 430, 241, 16))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.edit_nickname = QLineEdit(self.centralwidget)
        self.edit_nickname.setObjectName(u"edit_nickname")
        self.edit_nickname.setGeometry(QRect(10, 450, 121, 22))
        self.btn_send = QPushButton(self.centralwidget)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setGeometry(QRect(10, 480, 361, 24))
        self.btn_send.setFont(font)
        self.edit_text = QLineEdit(self.centralwidget)
        self.edit_text.setObjectName(u"edit_text")
        self.edit_text.setGeometry(QRect(150, 450, 221, 22))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hun's_Messenger", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ub2c9\ub124\uc784", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ucc44\ud305 \ub0b4\uc6a9", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"\uc804\uc1a1", None))
    # retranslateUi

