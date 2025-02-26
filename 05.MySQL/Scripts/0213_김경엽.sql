use sqlclass_db;


# 테이블 생성

create table authors (
	author_id INT not NULL auto_increment,
	firstname varchar(20),
	lastname varchar(30),
	primary key(author_id)
);

# 테이블에 데이터 넣기
insert into authors( author_id, firstname, lastname)
values (1, 'Paul', 'Deirel'),
		(2, 'Harvey','Deitel'),
		(3,'Abbey','Deitel'),
		(4,'Dan','Quirk'),
		(5,'Micheal','Morgano');

# authors 테이블 데이터 확인
select * from authors


# titles 테이블 만들기

create table titles(
	isbn varchar(20),
	title varchar(100),
	edition_number	INT,
	copyright varchar(4),
	primary key(isbn)
);

# title 테이블에 데이터 넣기
# 
insert into titles(isbn, title, edition_number, copyright)
values
('0132151006' ,'Internet & World Wide Web How to Program',5,'2012'),
('0133807800' ,'Java How to Program',10,'2015'),
('0132575655' ,'Java How to Program, Late Objects Version',10,'2015'),
('013299044X' ,'C How to Program',7,'2013'),
('0132990601' ,'Simply Visual Basic 2010',4,'2013'),
('0133406954' ,'Visual Basic 2012 How to Program',6,'2014'),
('0133379337' ,'Visual C# 2012 How to Program',5,'2014'),
('0136151574' ,'Visual C++ How to Program',2,'2008'),
('0133378713' ,'C++ How to Program',9,'2014'),
('0133764036' ,'Android How to Program',2,'2015'),
('0133570924' ,'Android for Programmers: An App-Driven Approach, Volume 1',2,'2014'),
('0132121360' ,'Android for Programmers: An App-Driven Approach',1,'2012');


# author_isbn 테이블 

drop table author_isbn;
create table   author_isbn(
   author_id INT not NULL auto_increment,
   isbn VARCHAR(20),
   foreign key (author_id) references authors(author_id),
   foreign key (isbn) references titles(isbn));

insert into author_isbn (author_id,isbn)
values(1,'0132151006'),
(2,'0132151006'),
(3,'0133807800'),
(1,'0132575655'),
(2,'013299044X'),
(1,'013299044X'),
(2,'0132575655'),
(1,'013299044X'),
(2,'013299044X'),
(1,'0132990601'),
(2,'0132990601'),
(3,'0132990601'),
(1,'0133406954'),
(2,'0133406954'),
(3,'0133406954'),
(1,'0133379337'),
(2,'0133379337'),
(1,'0136151574'),
(2,'0136151574'),
(4,'0136151574'),
(1,'0133378713'),
(2,'0133378713'),
(1,'0133764036'),
(2,'0133764036'),
(3,'0133764036'),
(1,'0133570924'),
(2,'0133570924'),
(3,'0133570924'),
(1,'0132121360'),
(2,'0132121360'),
(3,'0132121360'),
(5,'0132121360');


#1. 저작권 2013년 이후 도서 출력

select title, edition_number, copyright from titles
where copyright >= 2013 ORDER by copyright DESC;


#2. ‘D’로 시작하는 저자 이름 출력


select author_id, firstname, lastname from authors
where lastname like 'D%';

#3. 저자 이름의 두번째 글자가 'o'를 포함하는 저자 이름 출력
select author_id, firstname, lastname from authors
where lastname like '_o%';

#4. 저자 이름을 오름차순으로 정렬
select author_id, firstname, lastname from authors
ORDER by   firstname,lastname;

#5.책 제목에 ”How to Program＂을 포함하는 책 정보 출력
select isbn, title, edition_number, copyright
from titles
where title like '%How to Program%'
ORDER by title asc;



#6. 내부조인 #1
select a.firstname, a.lastname, b.isbn
from authors as a 
inner join author_isbn as b
	on a.author_id = b.author_id ORDER by firstname,lastname ASC;


# 7. 내부 조인 #2
select * from titles;
select * from author_isbn;

# 내림차순
select b.author_id, b.isbn,t.title, t.edition_number, t.copyright 
from titles  as t 
inner join author_isbn as b
	on t.isbn = b.isbn ORDER by isbn DESC;

#8. 3개의 테이블을 내부 조인
desc titles;
desc author_isbn; # MUL 중복가능
desc authors;

select a.firstname, a.lastname, t.title, b.isbn, t.copyright
from authors as a
	inner join author_isbn as b 
	on a.author_id = b.author_id
	inner join titles as t 
	on b.isbn = t.isbn
where a.lastname ='Quirk';

# 문제 9. 3개의 테이블을 내부 조인


select a.firstname, a.lastname, t.title, b.isbn, t.copyright
from authors as a
	inner join author_isbn as b 
	on a.author_id = b.author_id
	inner join titles as t 
	on b.isbn = t.isbn
# where (a.firstname = 'Paul' or a.firstname = 'Harvey' ) and a.lastname ='Deitel' ;
where a.firstname = 'Paul' or a.firstname = 'Harvey';


# 문제 10   ‘Abbey	Deitel’과 ‘Harvey Deitel’이 공동 저자인 책 정보 출력

# 나중에 질문
-- select t.title, t.isbn, t.copyright 
-- from titles as t
-- 	inner join author_isbn as b 
-- 	on t.isbn = b.isbn
----------------------------------------------------------------------
-- 	inner join authors as a 
-- 	on b.author_id = a.author_id 
-- where (a.firstname = 'Abbey' and  a.firstname = 'Harvey');

select t.title, b.isbn, t.copyright 
from titles as t
	inner join author_isbn as b on t.isbn = b.isbn
	inner join authors as a1on b.author_id  = a1.author_id 
	inner join author_isbn as b2 on t.isbn = b2.isbn
	inner join authors as a2 on b2.author_id  = a2.author_id 
where (a1.firstname = 'Abbey' and  a1.lastname = 'Deitel')
	and (a2.firstname = 'Harvey' and  a2.lastname = 'Deitel');
	




