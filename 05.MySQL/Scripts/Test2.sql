use sqlclass_db;


drop table if exists person;

create table person
	(person_id smallint UNSIGNED,
	fname VARCHAR(20),
	lname varchar(20),
	eye_color ENUM('BR', 'BL','GR'),
	birth_date DATE,
	street VARCHAR(30),
	city VARCHAR(20),
	state VARCHAR(20),
	country VARCHAR(20),
	postal_code VARCHAR(20),
	primary key (person_id)
	);

desc person;


drop table if exists favorite_food;

create table favorite_food
(
	person_id smallint UNSIGNED,
	food VARCHAR(20),
	primary key (person_id, food),
	foreign key(person_id) references person(person_id)
	

);


set foreign_key_checks = 0;

alter table person modify person_id smallint unsigned auto_increment;

set foreign_key_checks=1;

insert into person 
(person_id, fname, lname, eye_color, birth_date)
values( null, 'William','Turner','BR','1972-05-27');

select * from person;


select person_id, fname, lname, birth_date from person;

select person_id, fname, lname, birth_date
from person where lname = 'Turner';


insert into favorite_food (person_id, food)
values (1, 'pizza');

insert into favorite_food (person_id, food)
values (1,'cookies');

insert into favorite_food (person_id, food)
values (1,'nachos');

delete from favorite_food where person_id =1;

insert into favorite_food(person_id, food)
values  (1,'pizza'),
		(1,'cookie'),
		(1,'nachos');
	
select food from favorite_food
where person_id=1 order by food asc;

select food from favorite_food
where person_id=1 order  by food desc ;

insert into person
(person_id, fname, lname, eye_color, birth_date,
street, city,state,country, postal_code)
VALUES(null,'Susan','Smith','BL','1975-11-02',
'23 Maple St.','Arligton','VA', 'USA','20220');


SELECT person_id,fname,lname,birth_date FROM person;

update person
set street = '1225 Tremon St.',
	city = 'Boston',
	state ='MA',
	country ='USA',
	postal_code = '02138'
where person_id =1;

select * from person;
	
insert into person (person_id, fname, lname) values(3,'Kevin', 'kern'); 
insert into favorite_food (person_id, food) values(null,'Kevin','Kern');

select * from person;



