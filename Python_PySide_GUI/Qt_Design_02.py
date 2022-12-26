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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLayout,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
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
        self.radio_1 = QRadioButton(self.centralwidget)
        self.radio_1.setObjectName(u"radio_1")
        self.radio_1.setGeometry(QRect(110, 40, 91, 20))
        self.radio_2 = QRadioButton(self.centralwidget)
        self.radio_2.setObjectName(u"radio_2")
        self.radio_2.setGeometry(QRect(210, 40, 91, 20))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 170, 391, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.chk_1 = QCheckBox(self.widget)
        self.chk_1.setObjectName(u"chk_1")

        self.horizontalLayout.addWidget(self.chk_1)

        self.chk_2 = QCheckBox(self.widget)
        self.chk_2.setObjectName(u"chk_2")

        self.horizontalLayout.addWidget(self.chk_2)

        self.chk_3 = QCheckBox(self.widget)
        self.chk_3.setObjectName(u"chk_3")

        self.horizontalLayout.addWidget(self.chk_3)

        btn_Click.setCentralWidget(self.centralwidget)

        self.retranslateUi(btn_Click)

        QMetaObject.connectSlotsByName(btn_Click)
    # setupUi

    def retranslateUi(self, btn_Click):
        btn_Click.setWindowTitle(QCoreApplication.translate("btn_Click", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("btn_Click", u"Button", None))
        self.radio_1.setText(QCoreApplication.translate("btn_Click", u"Ready!", None))
        self.radio_2.setText(QCoreApplication.translate("btn_Click", u"Unready...", None))
        self.chk_1.setText(QCoreApplication.translate("btn_Click", u"Ready!", None))
        self.chk_2.setText(QCoreApplication.translate("btn_Click", u"Ready!", None))
        self.chk_3.setText(QCoreApplication.translate("btn_Click", u"Ready!", None))
    # retranslateUi

