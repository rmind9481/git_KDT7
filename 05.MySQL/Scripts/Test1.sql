use sqlclass_db;


drop table if exists books;

create table books(
	book_id INT not null auto_increment,
	title VARCHAR(50),
	publisher VARCHAR(30),
	year VARCHAR(10),
	price INT,
	primary KEY(book_id)
);


insert into books(title, publisher, year, price)
values ('Operating System Concepts', 'Wiley', '2023', 30700);

insert into books(title, publisher, year, price)
values ('Head First PHP and MySQL', 'OReilly', '2009', 58000);


insert into books(title, publisher, year , price)
values ('C Programming Language', 'PRentice-Hall', '1989',35000),
		('Head First SQL', 'QReilly', '2007', 43000),
		('Java How to PRogramming', 'Person', '2015', 65000);

select * from books;

select publisher from books;

select * fROM books where publisher = 'oreilly';

select * from books where price >= 30000 and price <= 50000

update books set price = 30000 where book_id=1;

select * from books;

update books
set title = 'Head First SQL 3rd Edition', price=45000 where year=2007;

select * from books where year =2007;

delete from books where book_id = 5;

select * from books;


# 컬럼 추가
alter TABLE books add author varchar(50);
desc books;

select * from books;

update books set author= 'John willey' where book_id=1;
update books set author= 'Beightely' where book_id=2;
update books set author= 'Brain' where book_id=3;
update books set author= 'Lynn' where book_id=4;

select * from books;


# 컬럼 삭제

alter table books drop column author;

select  * from books;