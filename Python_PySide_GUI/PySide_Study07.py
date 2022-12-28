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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pyperclip

def find(chrome, css_selector) :
    wait = WebDriverWait(chrome, 5)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Selenium 띄우기 테스트
        chrome = webdriver.Chrome("./Python_PySide_GUI/chromedriver.exe")

        # naver mail 로그인
        chrome.get("https://mail.naver.com")
        input_id = find(chrome, "#id")
        print(input_id)


if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())