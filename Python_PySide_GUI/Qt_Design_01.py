# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Qt_Design_01.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_btn_Click(object):
    def setupUi(self, btn_Click):
        if not btn_Click.objectName():
            btn_Click.setObjectName(u"btn_Click")
        btn_Click.resize(429, 210)
        self.centralwidget = QWidget(btn_Click)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 90, 171, 41))
        font = QFont()
        font.setFamilies([u"\ud734\uba3c\uc61b\uccb4"])
        font.setPointSize(16)
        self.pushButton.setFont(font)
        btn_Click.setCentralWidget(self.centralwidget)

        self.retranslateUi(btn_Click)

        QMetaObject.connectSlotsByName(btn_Click)
    # setupUi

    def retranslateUi(self, btn_Click):
        btn_Click.setWindowTitle(QCoreApplication.translate("btn_Click", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("btn_Click", u"Button", None))
    # retranslateUi

