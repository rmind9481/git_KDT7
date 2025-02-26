use sqlclass_db;
drop table if exists customer;

create table customer 
	( customer_id smallint unsigned,
	first_name varchar(20),
	last_name varchar(20),
	birth_date date,
	spouse_id smallint unsigned,
	primary key (customer_id));

# ------------------------------------------------------------------------------------------------



INSERT	INTO customer(customer_id,first_name,last_name,birth_date,spouse_id)
VALUES
(1,'John','Mayer','1983-05-12',2),
(2,'Mary','Mayer','1990-07-30',1),
(3,'Lisa','Ross','1989-04-15',5),
(4,'Anna','Timothy','1988-12-26',6),
(5,'Tim','Ross','1957-08-15',3),
(6,'Steve','Donell','1967-07-09',4);



INSERT INTO customer(customer_id,first_name,last_name,birth_date)
VALUES (7,'Donna','Trapp','1978-06-23');

select * from customer;

# 셀프조인
SELECT
	cust.customer_id,
	cust.first_name,
	cust.last_name,
	cust.birth_date,
	cust.spouse_id,
	spouse.first_name as spouse_firstname,
	spouse.last_name as spouse_lastname,
	spouse.birth_date as spouse_birthdate # 배우자의 생일 정보추가
FROM customer as cust
	inner JOIN customer as spouse
	#ON cust.spouse_id =	spouse.customer_id;
	on cust.customer_id = spouse.spouse_id;

# ----------------------------------------------------------------

use sakila;


select  'CUST' as type1, c.first_name, c.last_name
from customer c
union all
select 'ACTR' as type1, a.first_name, a.last_name
from actor a;

# ----------------------------------------------------------------
# customer 테이블 과 actor 테이블에서
# 'J' 와 'D' 로 시작하는 이름 검색후 
select 'cust' as type1, c.first_name , c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'
union all
select 'act' as type1, a.first_name, a.last_name
from actor a
where a.first_name like 'J%' and a.last_name like 'D%';


# ----------------------------------------------------------------


select c.first_name, c.last_name
from customer c
where c.first_name like 'D%' and c.last_name like 'T%'

select a.first_name, a.last_name
from actor a
where a.first_name like 'D%' and a.last_name like 'T%'



# ---------------------교집합

select c.first_name, c.last_name
from customer c
where c.first_name like 'D%' and c.last_name like 'T%'
INTERSECT
select a.first_name, a.last_name
from actor a
where a.first_name like 'D%' and a.last_name like 'T%'




# -------------------------------

select c.first_name, c.last_name
from customer as c
inner join actor as a
on (c.first_name = a.first_name)  and (c.last_name = a.last_name);


# -------------------------------
# EXCEPT 연산자
select a.first_name, a.last_name
from actor a
where a.first_name like 'J%' and a.last_name like 'D%'
EXCEPT
select c.first_name, c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'

# -------------------------------
# 복합 쿼리의 결과 정렬
select a.first_name fname, a.last_name lname
from actor a
where a.first_name like 'J%' and a.last_name like 'D%'
union all
select c.first_name, c.last_name
from customer c
where c.first_name like 'J%' and c.last_name like 'D%'
order by lname,fname;





