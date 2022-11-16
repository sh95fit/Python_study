# DB 연동 보충(sqlite3)
'''
입력을 받은 데이터를 DB에 저장하기
추후 통신을 통해 받아온 데이터 저장 시 활용!

fetchall() : 모든 row를 가져올 때 사용
fetchone() : 한 row를 가져올 때 사용(연속 사용 시 다음 row로 cursor 이동)
fetchmany(n) : n개만큼의 row를 가져올 때 사용
'''

import sqlite3

# insert문
'''
hak = input("학번 : ")
name = input("이름 : ")
major = input("전공 : ")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "INSERT INTO STUDENT(HAK, NAME, MAJOR) VALUES(?, ?, ?)"
cursor.execute(sql, (hak, name, major))
conn.commit()  # commit을 하지 않으면 execute에 의해 실행은 되지만 저장은 되지 않는다.
conn.close()
'''

'''
# select문
conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "SELECT * FROM STUDENT"
cursor.execute(sql)
#print(cursor.fetchone())  # 한 줄만 출력
#print(cursor.fetchall())   # 전체 출력 (리스트 내 튜플 형태로 출력)
for row in cursor.fetchall() :
    print("%s %s %s"%(row[0], row[1], row[2]))
cursor.close()
'''

'''
# select문 - 조건에 충족하는 자료만 읽어오기

hak = input("학번 : ")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "SELECT * FROM STUDENT WHERE HAK = ?"
cursor.execute(sql, (hak,))  # 조건에 해당하는 항목이 1개인 경우! 변수 뒤 콤마를 표시
#print(cursor.fetchone())
row = cursor.fetchone()
print("%s %s %s"%(row[0], row[1], row[2]))
cursor.close()
'''

'''
# update문 - 조건 충족되는 요소의 데이터 변경

hak = input("학번 : ")
name = input("변경 이름 : ")
major = input("변경 전공 : ")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "UPDATE STUDENT SET NAME = ?, MAJOR = ? WHERE HAK = ?"
cursor.execute(sql, (name, major, hak))
conn.commit()
conn.close()
'''

'''
# delete문 - 조건 충족 데이터 삭제

hak = input("학번 : ")

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
sql = "DELETE FROM STUDENT WHERE HAK = ?"
cursor.execute(sql, (hak,))
conn.commit()
conn.close()
'''