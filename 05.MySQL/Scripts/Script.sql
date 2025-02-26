use sakila;

show tables;

use sqlclass_db;

# book 테이블이 있으면 삭제
drop table if exists books; 
drop table if exists books;


create table books (
	book_id INT not null auto_increment,
	title VARCHAR(50),
	publisher VARCHAR(30),
	year VARCHAR(10),
	price INT,
	primary KEY(book_id)
);



