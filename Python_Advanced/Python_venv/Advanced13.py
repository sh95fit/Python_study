# 데이터베이스
'''
* 데이터베이스란?
구조화된 데이터의 집합
데이터 삽입, 조회, 수정, 삭제를 통한 데이터 관리가 가능함

* 데이터베이스
테이블의 집합

* 테이블
한 단위의 데이터 기록(record)
행(row)의 집합 (행 = 레코드(record))

* 열(column)
데이터의 항목(field)
열 = 필드(field)

* DBMS
Database Management System
데이터베이스를 관리해주는 시스템
ex> MySQL, Oracle, sqlite

클라이언트 -> SQL -> DB서버
클라이언트 <- 응답 <- DB서버

* SQL이란?
Structured Query Language
데이터베이스를 관리하기 위해 사용되는 언어

SQL 종류
DDL(Data Definition Language) : 데이터 정의 언어
DML(Data Manipulation Language) : 데이터 조작 언어
'''

# SQL DDL(CREATE, ALTER, DROP)
'''
* SQLite 데이터 타입 4가지
 - integer 정수
 - real 실수
 - text 문자열
 - null num값(데이터 없음)

* SQL CREATE
 - 테이블 생성 명령(쿼리)
 - 형태
   CREATE TABLE 테이블명 (컬럼명1 데이터타입, 컬럼명2 데이터타입);
   ex> CREATE TABLE post(id integer, title text, content text);
 - 제약 조건
  1. primary key : 기본 키 / 레코드를 구분 짓는 값!
   : 형태 - 데이터 타입 뒤에 정의
     ex> CREATE TABLE post(id integer primary key, ...)
  2. not null
   : 형태 - 데이터 타입 뒤에 정의
     ex> CREATE TABLE post(컬럼명1 데이터타입 not null, ...)
  3. default : 기본값
   : 형태 - 데이터 타입 뒤에 정의
     ex> CREATE TABLE 테이블명(컬럼명1 데이터타입 default '제목없음', ...)
  4. unique : 유니크 / 유일한 값
   : 형태 : 데이터 타입 뒤에 정의
     ex> CREATE TABLE user(id integer primary key autoincrement, nickname text unique);

* SQL ALTER
 - 테이블 수정 명령(쿼리)
 - 형태
   ALTER TABLE 테이블명 RENAME TO 새로운 테이블명;
   ex> ALTER TABLE post RENAME TO board;
 - 테이블 컬럼 수정
 - 형태
   ALTER TABLE 테이블명 ADD COLUMN 컬럼명;
   ex> ALTER TABLE board ADD COLUMN post_date;
'''

# SQLite에서 실행!
'''
#SQL_DDL - post 테이블 생성
CREATE TABLE post(id integer primary key, title text not null default '제목없음', content text default '제목없음');
DROP TABLE post;

#SQL_DDL - user 테이블 생성
CREATE TABLE user(id integer primary key autoincrement, nickname text unique);

#SQL_DDL - 테이블 수정(테이블명 변경)
ALTER TABLE post RENAME TO board;

#SQL_DDL - 테이블 수정(column(열) 추가)
ALTER TABLE board ADD COLUMN post_date text;

#SQL_DDL - 테이블 수정(column(열) 삭제)
ALTER TABLE board DROP COLUMN post_date;

#SQL_DDL - 테이블 수정(column(열) 이름 변경)
ALTER TABLE board RENAME COLUMN post_date TO reg_date;
'''