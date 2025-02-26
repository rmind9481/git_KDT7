/*  
 * 과제 2. 노벨상 수상자
 */

use sqlclass_db;

select * from nobel;

#select year from nobel order by year asc;

# 1번. 1960년 Physics와 Peace 노벨 수상자 출력 
SELECT year, category, fullname
  FROM nobel
 WHERE year = 1960 AND (category = 'Physics' or  category='Peace');


# 2번. Albert Einstein이 수상한 연도와 제목 
SELECT year, category, prize_amount, birth_continent, birth_country
  FROM nobel
WHERE fullname = 'Albert Einstein';

SELECT year, category, prize_amount, birth_continent, birth_country
  FROM nobel
WHERE fullname = 'albert einstein';

# 3번. 1910~2010년까지노벨평화상 수상자 명단을 연도순으로 정렬 후 출력  
select year, fullname, birth_country 
from nobel 
where category='Peace' and year between 1910 and 2010 
order by year asc;

# 4번. 노벨상 수상자 중에서 'John'으로 시작하는 수상자 명단 
SELECT category, fullname FROM nobel
  WHERE fullname LIKE 'John%';
 
# 5번. 1964년 수상자 중에서 노벨화학상과 의학상을 제외한 수상자 정보 출력 
# 이름을 기준으로 오름차순 정렬  

 SELECT * FROM nobel
  WHERE year = 1964
    AND category NOT IN ('Chemistry','Physiology or Medicine')
  order by fullname asc;

# 6번. 2000년부터 2019년까지 노벨 문학상 수상자 출력 
SELECT year, fullname, gender, birth_country FROM nobel
  WHERE category = 'Literature' and (year between 2000 and 2019)
 order by year;
 

 # 7번. 각 분야별 역대 수상자 수를 출력 
select category, count(category) from nobel 
group by category 
order by count(category) desc;

# 8-1번. 노벨 의학상이 있었던 연도 출력 
select DISTINCT year FROM nobel 
WHERE category = 'Physiology or Medicine';

# 8-2번. 노벨 의학상이 없었던 연도 출력 
select distinct year
from nobel
where year 
not in (select year from nobel where category = 'Physiology or Medicine');

# 9번. 노벨 의학상이 없었던 연도의 횟수 출력 
SELECT count(distinct year) as no_medicine_count FROM nobel
WHERE year 
NOT IN (SELECT DISTINCT year FROM nobel WHERE category = 'Physiology or Medicine');
 
# 10번. 여성 노벨 수상자의 명단을 출력 (연도, 분야, 이름, 출생국)
select fullname,  category, birth_country 
from nobel 
where gender='female';


# 11번. 출생 국가별로 그룹화 (출생 국가명, 수상빈도수) 출력 
select birth_country, count(birth_country) from nobel
group by birth_country;

# 12번 수상자의 출생국가가 'Korea'인 정보 모두 출력  
select * from nobel 
where birth_country='Korea';

# 13번. 수상자의 대륙이 (Europe, North America, null)이 아닌 정보 출력 
select * from nobel
where birth_continent not in ('Europe', 'North America', '');

# 14번. 수상자의 국가별로 그룹화를 해서 수상횟수가 10회 이상인 국가만 출력 
# group by, having, order by 사용 

select birth_country, count(*) as count
from nobel 
group by birth_country 
having count(*) >=10 order by count desc;

# 15번. 2회 이상 수상자 중에서 fullname이 공백이 아닌 경우 출력  
select fullname, count(*) as num 
from nobel 
group by fullname 
having (count(*) >= 2) and (fullname <> '')
order by fullname asc;


# 16번. 
# List the winners, year and subject where the winner starts with Sir. 
# Show the the most recent first, then by name order.
SELECT winner, yr, subject
FROM nobel
WHERE winner LIKE 'sir%'
ORDER BY yr DESC, winner
