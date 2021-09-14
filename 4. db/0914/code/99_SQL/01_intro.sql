-- 주석
/* 여러 줄 주석
    입니다
    히히
    SQL 구문은 대소문자 구분이 없음! (중요)
    기본 문법: 변하지 않는 부분은 대문자, 변하는 부분은 소문자
 */
-- 데이터 전체 조회: SELECT
SELECT * FROM examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- 테이블 삭제
DROP TABLE classmates;

CREATE TABLE classmates (
-- id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 데이터 입력
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');

SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates;

-- 데이터 삭제
DELETE FROM classmates WHERE rowid=5;

-- 데이터 수정
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;


CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age>=30;
SELECT first_name FROM users WHERE age>=30;
SELECT age, last_name FROM users WHERE age>=30 AND last_name='김';

SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age>=30;
SELECT first_name, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age>=30;

SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%5114%';

SELECT * FROM users ORDER BY age LIMIT 10;

-- -----------------------------------------
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번내용');

ALTER TABLE articles RENAME TO news;

ALTER TABLE news ADD COLUMN created_at TEXT;  -- (i) NOT NULL 없이
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT 'default';  -- (ii) DEFAULT 설정