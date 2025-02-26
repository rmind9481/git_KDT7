use sakila;

select customer_id, count(*)
from rental
group by customer_id ;

#--------------------------------------------------------------

select customer_id, count(*)
from rental
group by customer_id
order by 2 desc;


#---------------------------------------------------------------

select customer_id, count(*)
from rental
group by customer_id 
having count(*) >= 40;

# -------------------------------------------------------------

SELECT max(amount)	as max_amt,
min(amount)	as min_amt,
avg(amount)	as avg_amt,
sum(amount)	as tot_amt,
count(*)	as num_payments
FROM payment;


# ----------------------------------------------------------
SELECT customer_id,
max(amount)	as max_amt,
min(amount)	as min_amt,
avg(amount)	as avg_amt,
sum(amount)	as tot_amt,
count(*)	as num_payments
FROM payment
GROUP	BY customer_id;

# -----------------------------------------------------------

SELECT count(customer_id)	as num_rows,
count(distinct customer_id)	as num_customers
FROM payment;


# ------------------------------------------------------------
SELECT max(datediff(return_date,	rental_date))
FROM rental;

# ------------------------------------------------------------
SELECT avg(datediff(return_date,	rental_date))	FROM rental;

# ------------------------------------------------------------
use sqlclass_db;
create  table number_tbl ( val smallint);
desc number_tbl;

INSERT	INTO number_tbl VALUES(1);
INSERT	INTO number_tbl VALUES(3);
INSERT	INTO number_tbl VALUES(5);

select * from number_tbl;

SELECT count(*)	as num_rows,
count(val)	as num_vals,
sum(val)	as total,
max(val)	as max_val,
avg(val)	as avg_val
FROM number_tbl;


# ------------------------------------

INSERT	INTO number_tbl VALUES (NULL);
SELECT *	FROM number_tbl;


SELECT count(*)	as num_rows,
count(val)	as num_vals,
sum(val)	as total,
max(val)	as max_val,
avg(val)	as avg_val
FROM number_tbl;

# -------------------------------------

SELECT fa.actor_id,	f.rating,count(*)
from film_actor as fa
inner JOIN film as f
ON fa.film_id =	f.film_id
group by fa.actor_id,f.rating
order BY 1,2;

# ------------------------------------------------------
extract (unit, from date)

#연도별 대여 횟수를 그룹화
SELECT extract(year from rental_date)	as year,
count(*)	as how_many
FROM rental
GROUP	BY extract(year from rental_date);

# ------------------------------------------------------
# 각 배우/등급의 총합과 각 개별 배우의 총합 계산
select fa.actor_id, f.rating, count(*)
from film_actor as fa
	inner join film as f
	on fa.film_id = f.film_id
group by fa.actor_id, f.rating with rollup
order by 1, 2;


# -----------------------------------------------------
select fa.actor_id, f.rating, count(*)
from film_actor fa
	inner join film f
	on fa.film_id = f.film_id
where f.rating in ('G', 'PG')
group by fa.actor_id, f.rating 
having count(*) > 9; 


# 2단계
select fa.actor_id, f.rating, count(*)
from film_actor fa
	inner join film f
	on fa.film_id = f.film_id
where f.rating in ('G', 'PG')
group by fa.actor_id, f.rating
order by 1;



#8.4 그룹 필터 조건


# 1단계: inner join과 필터링 (P, PG) 등
-- SELECT fa.actor_id, f.rating, f.title
-- FROM film_actor fa
--    INNER JOIN film f
--    ON fa.film_id = f.film_id
-- WHERE f.rating IN ('G','PG');


# 2단계: actor_id와 rating으로 그룹화
# count(*): 각 actor_id별 rating(영화등급)의 횟수
-- SELECT fa.actor_id, f.rating, count(*)
-- FROM film_actor fa
--    INNER JOIN film f
--    ON fa.film_id = f.film_id
-- WHERE f.rating IN ('G','PG')
-- GROUP BY fa.actor_id, f.rating
-- ORDER BY 1;


# 3단계
-- SELECT fa.actor_id, f.rating, count(*)
-- FROM film_actor fa
--    INNER JOIN film f
--    ON fa.film_id = f.film_id
-- #WHERE f.rating IN ('G','PG')
-- GROUP BY fa.actor_id, f.rating
-- HAVING count(*) >= 10
-- ORDER BY 1;
