# PySide 실습 - 메일 뷰어
'''
GUI
성능 이슈가 큰 문제이므로 성능적인 측면 개선을 위해 힘써야한다
변경성이 크므로 유지보수 측면을 중점적으로 검토하여야한다

크롤링 + PySide 접목하여 메일 뷰어 만들어보기
'''

import sys
import time
import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import PySide6.QtWidgets 
from Qt_Mailviewer import Ui_MainWindow

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pyperclip

from PySide_info import id_info, pw_info, daum_id, daum_pw

def find(chrome, css_selector) :
    wait = WebDriverWait(chrome, 15)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

def find_all(chrome, css_selector) :
    find(chrome, css_selector)
    return chrome.find_elements(By.CSS_SELECTOR, css_selector)

mails = []

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Selenium 띄우기 테스트
        chrome = webdriver.Chrome("./Python_PySide_GUI/chromedriver.exe")
        self.chrome = chrome

        # naver mail 로그인 및 메일 가져오기
        chrome.get("https://mail.naver.com")
        input_id = find(chrome, "#id")
        input_pw = find(chrome, "#pw")

        pyperclip.copy(id_info)
        time.sleep(1)
        input_id.click()
        input_id.send_keys(Keys.CONTROL, "v")

        pyperclip.copy(pw_info)   
        time.sleep(1)
        input_pw.click()
        input_pw.send_keys(Keys.CONTROL, "v")
        input_pw.send_keys("\n")

        for mail in find_all(chrome, "ul.mail_list li.mail_item") :
            date = mail.find_element(By.CSS_SELECTOR, "div.mail_date_wrap span.mail_date").text
            # 서로 다른 날짜 형태를 동일한 형태로 맞추기 (08:55와 12-28 08:55 두 가지 모두 인식 필요)
            now = datetime.datetime.now()
            if len(date) < 10 :
                date = f"{now.month}.{now.day} {date[2:]}"
            date = f"{now.year} {date}"
            date = datetime.datetime.strptime(date, "%Y %m.%d %H:%M")
            site = "네이버" # 고정값
            sender = mail.find_element(By.CSS_SELECTOR, "div.mail_sender button.button_sender").get_attribute("title")
            status = mail.find_element(By.CSS_SELECTOR, "div.mail_sender label[for*='read_'] span.blind").text
            title = mail.find_element(By.CSS_SELECTOR, "div.mail_inner div.mail_title span.blind").text
            link = mail.find_element(By.CSS_SELECTOR, "div.mail_inner div.mail_title a").get_attribute("href")
            
            mails.append({
                "date" : date,
                "site" : site,
                "sender" : sender,
                "status" : status,
                "title" : title,
                "link" : link,
            })

        # 다음 로그인, 메일 가져오기
        chrome.get("https://accounts.kakao.com/login/?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fmail.daum.net%252F")
        input_id = find(chrome, "#input-loginKey")
        input_pw = find(chrome, "#input-password")

        pyperclip.copy(daum_id)
        time.sleep(1)
        input_id.click()
        input_id.send_keys(Keys.CONTROL, "v")

        pyperclip.copy(daum_pw)
        time.sleep(1)
        input_pw.click()
        input_pw.send_keys(Keys.CONTROL, "v")
        input_pw.send_keys("\n")

        for m in find_all(chrome, "ul.list_mail li.mail_item") :
            date = m.find_element(By.CSS_SELECTOR, "span.txt_date").text
            date = datetime.datetime.strptime(date.strip(), "%y.%m.%d %H:%M")
            site = "다음"
            sender = m.find_element(By.CSS_SELECTOR, "div.info_from a").text
            status = m.find_element(By.CSS_SELECTOR, "div.info_mail a.btn_read span.img_mail").text
            title = m.find_element(By.CSS_SELECTOR, "div.info_subject strong.tit_subject").text
            link = m.find_element(By.CSS_SELECTOR, "div.info_subject a.link_subject").get_attribute("href")

            mails.append({
                "date": date,
                "site": site,
                "sender": sender,
                "status": status,
                "title": title,
                "link": link,
            })
 
        # 네이버 메일 테이블에 표시
        # 보낸이, 제목 부분 늘리기
        self.ui.table.horizontalHeader().setSectionResizeMode(2, PySide6.QtWidgets.QHeaderView.ResizeToContents)
        self.ui.table.horizontalHeader().setSectionResizeMode(4, PySide6.QtWidgets.QHeaderView.ResizeToContents)

        self.ui.table.setRowCount(len(mails))
        for r, m in enumerate(mails) :
            self.ui.table.setItem(r, 0, QTableWidgetItem(str(m["date"])))
            self.ui.table.setItem(r, 1, QTableWidgetItem(m["site"]))
            self.ui.table.setItem(r, 2, QTableWidgetItem(m["sender"]))
            self.ui.table.setItem(r, 3, QTableWidgetItem(m["status"]))
            self.ui.table.setItem(r, 4, QTableWidgetItem(m["title"]))

        # 제목 클릭 시 링크 주소로 이동!
        self.ui.table.cellDoubleClicked.connect(self.open_mail)
    
    def open_mail(self, r, c) :
        mail = mails[r]
        link = mail["link"]

        self.chrome.get(link)

        # 네이버, 다음 컨텐츠 경로 분기
        if mail["site"] == "네이버" :
            content = find(self.chrome, "div.mail_view_contents_inner").text
        elif mail["site"] == "다음" :
            content = find(self.chrome, "div.txt_mailview").text

        # 컨텐츠 내용 가져오기
        self.ui.lb_title.setText(mail["title"])
        self.ui.lb_content.setText(content)

if __name__ == "__main__" :
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

    