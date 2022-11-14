# DB 기초 - sqlite3
import sqlite3

conn = sqlite3.connect('C:/Users/tpgns/Desktop/Python_Study/Python_Basic/test.db')
cursor = conn.cursor()     # DB는 행과 열로 되어 있어 커서를 통해 움직여야 한다.

#조회
cursor.execute("SELECT * FROM School")
print(cursor.fetchall())   #fetchone : 1줄만 읽어옴 / fetchall : 전체를 읽어옴
# print(cursor.fetchone())

conn.commit()
conn.close()


#삽입
conn = sqlite3.connect('C:/Users/tpgns/Desktop/Python_Study/Python_Basic/test.db')
cursor = conn.cursor()


sql = "INSERT INTO School(S_NM) VALUES('A대학')"
cursor.execute(sql)

conn.commit()
conn.close()

#수정
conn = sqlite3.connect('C:/Users/tpgns/Desktop/Python_Study/Python_Basic/test.db')
cursor = conn.cursor()

sql = "UPDATE School SET S_NM = 'A대학교' WHERE S_NM = 'A대학'"
cursor.execute(sql)

conn.commit()
conn.close()

#삭제
conn = sqlite3.connect('C:/Users/tpgns/Desktop/Python_Study/Python_Basic/test.db')
cursor = conn.cursor()

sql = "DELETE FROM School WHERE S_NM = 'A대학교'"
cursor.execute(sql)

conn.commit()  # commit을 하지 않으면 저장이 되지 않음
conn.close()