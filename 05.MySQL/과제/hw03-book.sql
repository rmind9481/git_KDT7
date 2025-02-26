use sqlclass_db;

# authors 테이블 삭제 후 생성 
drop table if exists authors;

create table authors (
	author_id int not null,
	firstname varchar(20) not null,
	lastname varchar(30) not null,
	primary key(author_id)
);
	
# authors 테이블에 데이터 추가 
INSERT INTO authors 
	(author_id, firstname, lastname)
VALUES 
   (1, 'Paul','Deitel'), 
   (2, 'Harvey','Deitel'),
   (3, 'Abbey','Deitel'), 
   (4, 'Dan','Quirk'),
   (5, 'Michael','Morgano');

  
  
# titles 테이블 삭제 후 생성 
drop table if exists titles;

create table titles (
   isbn varchar (20) not null,
   title varchar (100) not null,
   edition_number INT not null,
   copyright varchar (4) not null,
   PRIMARY KEY (isbn)
);


INSERT INTO titles (isbn, title, edition_number, copyright)
VALUES
   ('0132151006','Internet & World Wide Web How to Program',5,'2012'),
   ('0133807800','Java How to Program',10,'2015'),
   ('0132575655','Java How to Program, Late Objects Version',10,'2015'),
   ('013299044X','C How to Program',7,'2013'), 
   ('0132990601','Simply Visual Basic 2010',4,'2013'),
   ('0133406954','Visual Basic 2012 How to Program',6,'2014'),
   ('0133379337','Visual C# 2012 How to Program',5,'2014'),
   ('0136151574','Visual C++ How to Program',2,'2008'),
   ('0133378713','C++ How to Program',9,'2014'),
   ('0133764036','Android How to Program',2,'2015'),
   ('0133570924','Android for Programmers: An App-Driven Approach, Volume 1',2,'2014'),
   ('0132121360','Android for Programmers: An App-Driven Approach',1,'2012');

  
# author_isbn 테이블 삭제 후 생성 
drop table if exists author_isbn;
create table author_isbn (
	author_id int not null,
	isbn varchar(20) not null,
	foreign key (author_id) references authors(author_id),
	foreign key (isbn) references titles(isbn)
);


INSERT INTO author_isbn (author_id,isbn)
VALUES
   (1,'0132151006'),
   (2,'0132151006'),
   (3,'0132151006'),
   (1,'0133807800'),
   (2,'0133807800'),
   (1,'0132575655'),
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
  
  
# 문제 1.
# 저작권이 2013년 이후인 필드 모두 출력 
select title, edition_number, copyright 
from titles 
where copyright >= '2013'
order by copyright desc;
  
# 문제 2.
# authors 테이블에서 'D'로 시작하는 저자의 이름 모두 출력   
select author_id, firstname, lastname 
from authors 
where lastname like 'D%';

# 문제 3.
# 저자의 lastname의 두 번째 글자에 'o'를 포함하는 저자 출력 
select author_id, firstname, lastname 
from authors 
where lastname like '_o%';
  
  
# 문제 4.
# 저자의 lastname, firstname 순으로 오름차순 정렬 후 출력 
select author_id, firstname, lastname 
from authors 
order by lastname, firstname;
  
  
# 문제 5
# titles 테이블에서 title 필드에 “How to Program”을 포함하는 책의 정보 출력
select isbn, title, edition_number, copyright 
from titles 
where title like '%How to Program%'
order by title asc;

# 문제 6
# authors 테이블과 author_isbn 테이블을 내부 조인
# join기준: author_id가 동일
# lastname, firstname 기준 오름차순 
select firstname, lastname, isbn 
from authors 
inner join author_isbn 
on authors.author_id = author_isbn.author_id 
order by lastname, firstname;


# 문제 7 
# author_isbn 테이블과 titles 테이블 내부 조인 
# isbn 오름 차순 정렬 
select ai.author_id, ti.isbn, ti.title, ti.edition_number, ti.copyright 
from author_isbn as ai 
inner join titles as ti 
on ai.isbn = ti.isbn  
order by ai.isbn desc;

# 문제 8 
# authors 테이블과 author_isbn 테이블 조인 
# author_isbn 테이블과 titles 테이블 조인 

select a.firstname, a.lastname,  ti.title, ti.isbn, ti.copyright 
from authors as a 
	inner join author_isbn as ai on a.author_id = ai.author_id 
	inner join titles as ti on ai.isbn = ti.isbn 
where (a.lastname ='Quirk');	

# 문제 9 
# 3개의 테이블 조인
# ‘Paul Deitel’과 ‘Harvel Deitel’이 쓴 책 정보 출력
select a.firstname, a.lastname,  ti.title, ti.isbn, ti.copyright 
from authors as a 
	inner join author_isbn as ai on a.author_id = ai.author_id 
	inner join titles as ti on ai.isbn = ti.isbn 
where (a.lastname ='Deitel' and a.firstname='Paul')
	or(a.lastname='Deitel' and a.firstname='Harvey');	


# 문제 10 
# 3개의 테이블 조인 
# ‘Paul Deitel’과 ‘Harvel Deitel’이 공동으로 쓴 책 정보 출력
select t.title, t.isbn, t.copyright 
from titles as t 	 
	inner join author_isbn as ai1 on t.isbn = ai1.isbn 
	inner join authors as a1 on ai1.author_id = a1.author_id 	
	inner join author_isbn as ai2 on t.isbn = ai2.isbn
	inner join authors as a2 on ai2.author_id = a2.author_id 
where ((a1.firstname ='Abbey' and a1.lastname='Deitel') 
   and (a2.firstname='Harvey' and a2.lastname='Deitel'));	


# 문제 10
select a1.firstname, a1.lastname, t.title, t.isbn, t.copyright 
from titles as t 	 
	inner join author_isbn as ai1 on t.isbn = ai1.isbn 
	inner join authors as a1 on ai1.author_id = a1.author_id 	
where (a1.firstname='Abbey' and a1.lastname='Deitel');


select a2.firstname, a2.lastname, t.title, t.isbn, t.copyright 
from titles as t 	 
	inner join author_isbn as ai2 
	on t.isbn = ai2.isbn
	inner join authors as a2 
	on ai2.author_id = a2.author_id 
where ((a2.firstname ='Harvey') and (a2.lastname='Deitel'));	

  
  
