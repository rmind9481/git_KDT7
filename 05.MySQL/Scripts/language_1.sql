use sakila;

select * from language;

select language_id, name, last_update from language;

select name from language;

select language_id,
	'COMMON' language_usage,
	language_id * 3.14 lang_pi_value,
	upper(name) language_name
from language;


select actor_id from film_actor order by actor_id;

# 중복제거

select distinct actor_id from film_actor order by actor_id;

# ----------------------------------------------------------
# 3.4 From 절
select first_name, last_name, email
from customer 
where first_name = 'JESSIE'

# 쿼리문
select concat(cust.last_name,',', cust.first_name) as 전체이름, cust.email as 이메일 
from
	(select first_name, last_name, email
	from customer
	where first_name = 'JESSIE' ) as cust;

# ----------------------------------------------------------------------------
# 임시 테이블
create temporary table actors_j
	(actor_id smallint(5),
	firtst_name varchar(45),
	last_name varchar(45));


desc actors_j;
	
# 실제 존하하는 actor 테이블에서 데이터를 가져옴

select actor_id, first_name, last_name
from actor where last_name like 'J%';


# 내부 쿼리의 결과를 actors_j 테이블에 데이터 추가
insert into actors_j
	select actor_id, first_name, last_name
	from actor where last_name like 'j%';

select * from actors_j;

# 가상테이블

create view cust_vw as
	select customer_id, first_name, last_name, active
	from customer;

select  * from cust_vw;

# 
select first_name, last_name
from cust_vw where active=0;

drop view cust_vw;

# ------------------------------------------------------------

select customer.first_name, customer.last_name,
time(rental.rental_date) as rental_time
from customer inner join rental 
	on customer.customer_id = rental.customer_id 
where date(rental.rental_date) = '2005-06-14';

# 조인한것 확인

# customer 과 rental 테이블 내부 조인후 모든 컬럼 출력
select *
from customer inner join rental
	on customer.customer_id = rental.customer_id ;

# 조인 이후 검색 조건추가: 모든 컬럼 출력
select *
from customer inner join rental
	on customer.customer_id = rental.customer_id
# 검색 조건이 2005-06-14인 경우
where date(rental.rental_date) = '2005-06-14';


select title
from film where rating='G' and rental_duration >=7;

# 
select title, rating, rental_duration
from film 
where (rating ='G' and rental_duration >= 7) or
	  (rating = 'PG-13' and rental_duration <4 );


# Group by 절과 having 절


select c.first_name, c.last_name, count(*) as rental_count
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id 
group by c.first_name, c.last_name
HAVING count(*) >= 40
order by count(*) desc;


# Order by 절

select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c inner join rental as r
	on c.customer_id  = r.customer_id 
where date(r.rental_date) = '2005-06-14'
order by c.last_name, c.first_name asc;

select c.first_name, c.last_name,
	time(r.rental_date) as rental_time
from customer as c inner join rental as r
	on c.customer_id  = r.customer_id 
where date(r.rental_date) = '2005-06-14'
order by time(r.rental_date) desc;

# ------------------------------------------------

select actor_id, first_name, last_name
from actor 
order by last_name, first_name;


# -------------------------------------------------
select actor_id, first_name, last_name
from actor 
where last_name = 'WILLIAMS'or last_name = 'DAVIS'

# -------------------------------------------------

select distinct customer_id
from rental
where date(rental_date) = '2005-07-05'

#---------------------------------------------------

select c.store_id, c.email, r.rental_date, r.return_date
from customer as c inner join rental as r
	on c.customer_id = r.customer_id 
where date(r.rental_date) = '2005-06-14'
order by return_date desc;

#----------------------------------------------------

select c.email, r.rental_date
from customer as c
	inner join rental as r
	on c.customer_id = r.customer_id 
where date(r.rental_date) != '2005-06-14';

# -----------------------------------------------------

select customer_id, rental_date
from rental
where rental_date <= '2005-6-16'
	and rental_date >='2005-06-14'

select customer_id, rental_date
from rental
where date(rental_date) = '2005-06-16'


# date()사용 : 2005년 6월 14 ~2005년 6월 16일까지 데이터 출력
select customer_id,rental_date
from rental
where date(rental_date) <= '2005-06-16' and
	date(rental_date) >= '2005-06-14';

select customer_id, rental_date
from rental
where date(rental_date) between '2005-06-14' and '2005-06-16'


select customer_id , payment_date, amount
from payment
where amount between 10.0 and 11.99

select last_name , first_name 
from customer
where last_name between 'FA' and 'FRB'

# --------------------------------------------------------

select  title, rating
from film 
where rating in ('G','PG');

# -------------------------------------------------------------------

select title, rating 
from film
where rating in (SELECT rating FROM film WHERE title like '%PET%');

select title, rating
from film
where rating not in ('PG-13', 'R','NC-17')

# -------------------------------------------------------------------

select last_name, first_name
from customer
where last_name like '_A_T%S'


# -------------------------------------------------------------------

select last_name, first_name
from customer
where last_name like 'Q%' or last_name like 'Y%';


# -------------------------------------------------------------------

select rental_id, customer_id, return_date
from rental
where return_date is null
or return_date not between '2005-05-01' and '2005-09-01'

# --------------------------------------------------------------------


select payment_id , customer_id , amount, date(payment_date) as payment_date
from payment p where (payment_id between 101 and 120);

# --------------------------------------------------------------------

