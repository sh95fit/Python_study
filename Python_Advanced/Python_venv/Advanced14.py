# 데이터베이스
# SQL DML
'''
SQL DML (조작어)
CRUD - INSERT, SELECT, UPDATE, DELETE


* INSERT - 데이터(행) 추가 명령
- INSERT INTO 테이블명 (컬럼명1, 컬럼명2) VALUES (값1, 값2);
- ex> INSERT INTO post (title, content) VALUES ('Python','Study');

* SELECT - 데이터 조회 명령
- SELECT 컬럼명1, 컬럼명2 FROM 테이블명;
- ex> SELECT * FROM post;   # 전체 조회

* SELECT문에 조건 추가! - WHERE
- SELECT 컬럼명1, 컬럼명2, FROM 테이블명 WHERE 조건;
  ex> SELECT title, content FROM post WHERE id=3;
- like : 특정 문자를 포함하는 조건을 줄 때 사용  (ex> '문자%' : '문자'로 시작하는 값만 추출)
  ex> SELECT * FROM post WHERE title like 'Advanced%';
- BETWEEN A AND B : 숫자들 중 A에서 B까지 범위를 만족하는 값 추출 시 사용
- IN : IN 우측에 포함되는 값만 추출
  ex> SELECT * FROM user WHERE address IN ('Seoul', 'Busan', 'Deagu');
- ORDER BY : 정렬(ASC : 오름차순, DESC : 내림차순)
  ex> SELECT * FROM 테이블명 ORDER BY 컬럼명 [ASC(디폴트값)|DESC];

* UPDATE - 데이터 수정 명령
- UPDATE 테이블명 SET 컬럼명=값, ... WHERE 조건식;
- ex> UPDATE post SET title = '제목 수정 중', content = '본문 수정 중' WHERE id=3;

* DELETE - 데이터 삭제 명령
- DELETE FROM 테이블명 WHERE 조건식;
- ex> DELETE FROM post WHERE id=3


데이터베이스 - GROUP BY, JOIN
* GROUP BY
- 그룹화하여 계산이 용이하도록 해줌
 ex> SELECT 컬럼명, count(*) FROM 테이블명 GROUP BY 컬럼명;
 ex> SELECT 컬럼명1, avg(컬럼명2) FROM 테이블명 GROUP BY 컬럼명1;

* Join
- 두 테이블을 묶어 조회할 때 사용
 ex> SELECT * FROM 테이블명1 INNER JOIN 테이블명2 WHERE 조건(ex> 테이블명1.컬럼1 = 테이블명2.컬럼2);
- Tip! INNER JOIN은 ,(콤마)로 대체할 수 있음!

파이썬에서 sqlite3 사용하기!
1. Database 파일 열기 - 2. 커서(Cursor) 생성 - 3. SQL 명령 생성 - 4. 커밋 또는 롤백 - 5. 데이터베이스 닫기

* INSERT, DELETE, UPDATE는 commit을 해야 실제 데이터베이스에 반영된다!!
'''

# 모듈 추가
import sqlite3

# 테이블 생성하기!
'''
# 데이터베이스 열기
conn = sqlite3.connect("./Python_Advanced/Python_venv/Database/SQL_STUDY.db")

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Item(
        id integer primary key autoincrement,
        code text not null,
        name text not null,
        price integer not null
    )
"""

# SQL 명령 실행
cur.execute(CREATE_SQL)

# 커밋
conn.commit()

# 데이터베이스 닫기
conn.close()
'''


# INSERT문
'''
# 데이터베이스 열기
conn = sqlite3.connect("./Python_Advanced/Python_venv/Database/SQL_STUDY.db")

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
INSERT_SQL = """
    INSERT INTO item(code, name, price) VALUES(?,?,?)
"""

# SQL 명령 실행
cur.execute(INSERT_SQL, ('A00001', '게이밍 마우스', 38000))

# 커밋
conn.commit()

# 데이터베이스 닫기
conn.close()
'''

# INSERT로 여러 데이터를 한번에 넣어야 하는 경우
'''
# 데이터베이스 열기
conn = sqlite3.connect("./Python_Advanced/Python_venv/Database/SQL_STUDY.db")

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
INSERT_SQL = """
    INSERT INTO item(code, name, price) VALUES(?,?,?)
"""

# 여러개의 데이터  - 중첩 튜플 형태!
data = {
  ('A00002', '에어컨 20평형', 350000),
  ('A00003', '최신형 스마트폰', 800000),
  ('A00004', '가성비 노트북', 650000)
}

# 여러개 데이터 추가 - 기존 튜플 자리에 중첩 튜플을 넘겨주면 executemany를 통해 여러개 데이터를 한번에 넣을 수 있다
cur.executemany(INSERT_SQL, data)

# 커밋
conn.commit()

# 데이터베이스 닫기
conn.close()
'''

# SELECT문
'''
# 데이터베이스 열기
conn = sqlite3.connect("./Python_Advanced/Python_venv/Database/SQL_STUDY.db")

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
SELECT_SQL = """
    SELECT * FROM item
"""

# SQL 명령 실행
cur.execute(SELECT_SQL)

# 데이터를 받아와 표출
rows = cur.fetchall()   # rows는 중첩 레코드

for row in rows :
  print(row)

# 데이터베이스 닫기
conn.close()
'''


# SELECT문
'''
# 데이터베이스 열기
conn = sqlite3.connect("./Python_Advanced/Python_venv/Database/SQL_STUDY.db")

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성 
# Tip! limit는 상위에서 몇 개의 데이터를 추출할 때 사용
SELECT_SQL = """
    SELECT * FROM item LIMIT 2   
"""

# SQL 명령 실행
cur.execute(SELECT_SQL)

# 데이터를 받아와 표출
rows = cur.fetchall()   # rows는 중첩 레코드

for row in rows :
  print(row)

# 데이터베이스 닫기
conn.close()
'''


# UPDATE문
'''
# 데이터베이스 열기
conn = sqlite3.connect("./Python_Advanced/Python_venv/Database/SQL_STUDY.db")

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성 
UPDATE_SQL = """
    UPDATE item SET price = 620000 WHERE code = 'A00002'
"""

# SQL 명령 실행
cur.execute(UPDATE_SQL)

# 커밋
conn.commit()

# 데이터베이스 닫기
conn.close()
'''


# DELETE문
# 데이터베이스 열기
conn = sqlite3.connect("./Python_Advanced/Python_venv/Database/SQL_STUDY.db")

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성 
DELETE_SQL = """
    DELETE FROM item WHERE code = 'A00002'
"""

# SQL 명령 실행
cur.execute(DELETE_SQL)

# 커밋
conn.commit()

# 데이터베이스 닫기
conn.close()




# 향후 공부 방향
'''
여러 개의 테이블이 필요한 DB 설계
Primary Key, Foreign Key 세팅
정규화(+역정규화) - 중복 제거 등
ERD(Entity Relationship Diagram) 작성
'''