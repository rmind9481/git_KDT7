use sqlclass_db;

drop table if exists string_tbl;
create table string_tbl
( char_fld char(30),
vchar_fld VARCHAR(30),
text_fld TEXT
);


insert into string_tbl (char_fld, vchar_fld, text_fld)
values ('This is char data',
'This is varchar data',
'This is text data');

select * from string_tbl;


# -----------------------------------------------


UPDATE string_tbl
SET vchar_fld =	'This is a piece of extremely long varchar data';

SELECT @@session.sql_mode;

# ansi 모드 확인
SET sql_mode='ansi';

# 변경사항 확인
SELECT @@session.sql_mode;


UPDATE string_tbl
SET vchar_fld =	'This is a piece of extremely long varchar data';

select * from string_tbl;

# 따옴표
update string_tbl
set text_fld =	'This string didn''t work, but it does now';

# quote() 내장함수
# 전체 문자열을 따옴표로 묶고, 문자열 내부의 작은 따옴표에 escape 문자를 추가

select quote(text_fld)
from string_tbl;


# length() 함수
# 테이블의 데이터 삭제
delete from string_tbl;

insert into string_tbl (char_fld, vchar_fld, text_fld)
values('This string is 28 characters',
		'This string is 28 characters',
		'This string is 28 characters');

select length(char_fld) as char_length,
	length(vchar_fld) as varchar_length,
	length(text_fld) as text_length
from string_tbl;


# 문자열 조작
#position() 부분 문자열 위치를 반환

SELECT position('characters' in vchar_fld)
FROM string_tbl;
#locate(‘문자열’, 열이름, 시작위치)


select * from string_tbl;

SELECT locate('is',	vchar_fld,	5)
FROM string_tbl;

SELECT locate('is',	vchar_fld,	1)	
FROM string_tbl;


delete from string_tbl;

INSERT INTO string_tbl(vchar_fld)
	VALUES ('abcd'),
	('xyz'),
	('QRSTUV'),
	('qrstuv'),
	('12345');
select vchar_fld from string_tbl order by vchar_fld;

select * from string_tbl;

# strcmp() 5개의 서로 다른 문자열 비교
SELECT strcmp('12345','1234') 12345_12345,
		strcmp('abcd','xyz') abcd_xyz,
		strcmp('abcd','QRSTUV') abcd_QRSTUV,
		strcmp('qrstuv','QRSTUV') qrstuv_QRSTUV,
		strcmp('12345','xyz') 12345_xyz,
		strcmp('xyz','qrstuv') xyz_qrstuv;


use sakila;


select name, name like '%y' as ends_in_y
from category;

select name, name regexp 'y$' as ends_in_y
from category;


# ------------------------------------

use sqlclass_db;

DELETE FROM string_tbl;
INSERT INTO string_tbl (text_fld)
VALUES ('This	string	was	29	characters');

# 문자열 합침 
UPDATE string_tbl
SET text_fld =	concat(text_fld,',but now it is longer');

select text_fld from string_tbl;

# concat() 함수 사용 


# insert() 함수 
# 4개의 인수로 구성
# 삽입
SELECT INSERT('goodbye	world',	9,0, 'cruel ')	as string;
# 교체
SELECT INSERT('goodbye	world', 1,7,'hello') as string;


# replace() 함수
# replace(문자열, 기존문자열, 새로운 문자열) 

select replace('goodbye world','goodbye', 'hello') as replace_str;


# substr() 또는 substring() 함수
select substr('goodbye cruel world', 9,5);



# -------------------------------
# cast() 예제

select cast('1456328' as signed integer);

select cast('20220101' as date);

select cast(now() as signed);


# 시간 데이터 처리
select cast('2019-09-17' as date) date_field,
		cast('108:17:57' as time) time_field;

# 날짜 생성 함수
# str_to_date(str_format)

select str_to_date('September 17,2019','%M %d, %Y') as return_date;

#
select str_to_date('04/30/2024', '%m/%d/%Y') as date1;

#일,월,연도 형태: 2024년 5일 1월
select str_to_date('01,5,2024', '%d,%m,%Y') as date2;

# 월,일,연도 형태 : 2024년 1월5일
select str_to_date('01,5,2024', '%m,%d,%Y') as date3;

# format 의 구성 요소의 순서에 따라 다른 날짜로 인식함





