-- Oracle
/* Write your PL/SQL query statement below */
with t (customer_id, min_year, max_year, yr_diff, yr_idx) as (
select customer_id,
       min(trunc(order_date, 'yyyy')) as min_year,
       max(trunc(order_date, 'yyyy')) as max_year,
       max(to_number(to_char(order_date, 'yyyy'))) - min(to_number(to_char(order_date, 'yyyy'))) + 1 as yr_diff,
       1 as yr_idx
from orders
group by customer_id
union all
select t.customer_id, t.min_year, t.max_year, yr_diff, yr_idx + 1
from t
where yr_idx + 1 <= yr_diff
),
t1 (customer_id, yr) as (
select customer_id, add_months(min_year, 12*(yr_idx - 1)) as yr
from t
),
t2 (customer_id, order_year, total_purchase) as (
select customer_id, trunc(order_date, 'yyyy') as order_year, sum(price) as total_purchase
from orders
group by customer_id, trunc(order_date, 'yyyy')
),
t3 (customer_id, yr, total_purchase, diff) as (
select t1.customer_id,
       t1.yr,
       coalesce(t2.total_purchase, 0) as total_purchase,
       coalesce(t2.total_purchase, 0)
       -
       lag(coalesce(t2.total_purchase, 0)) over (partition by t1.customer_id order by t1.yr) as diff
from t1
     left outer join t2 on (t2.customer_id = t1.customer_id and t2.order_year = t1.yr)
)
select distinct x.customer_id
from t3 x
where not exists (select null from t3 y where y.customer_id = x.customer_id and y.diff <= 0)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (customer_id, min_year, max_year, yr) as (
select customer_id,
       min(date_trunc('year', order_date)) as min_year,
       max(date_trunc('year', order_date)) as max_year,
       min(date_trunc('year', order_date)) as yr
from orders
group by customer_id
union all
select t.customer_id, t.min_year, t.max_year, t.yr + interval '1 year'
from t
where t.yr + interval '1 year' <= max_year
),
t1 (customer_id, order_year, total_purchase) as (
select customer_id,
       date_trunc('year', order_date) as order_year,
       sum(price) as total_purchase
from orders
group by customer_id, date_trunc('year', order_date)
),
t2 (customer_id, yr, total_purchase, diff) as (
select t.customer_id,
       t.yr,
       coalesce(t1.total_purchase, 0) as total_purchase,
       coalesce(t1.total_purchase, 0)
       -
       lag(coalesce(t1.total_purchase, 0)) over (partition by t.customer_id order by t.yr) as diff
from t
     left outer join t1 on (t1.customer_id = t.customer_id and t1.order_year = t.yr)
)
select distinct x.customer_id
from t2 x
where not exists (select null from t2 y where y.customer_id = x.customer_id and y.diff <= 0)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (customer_id, min_year, max_year, yr) as (
select customer_id,
       min(CONVERT(DATETIME, CONVERT(VARCHAR(4), order_date, 120) + '-01-01')) as min_year,
       max(CONVERT(DATETIME, CONVERT(VARCHAR(4), order_date, 120) + '-01-01')) as max_year,
       min(CONVERT(DATETIME, CONVERT(VARCHAR(4), order_date, 120) + '-01-01')) as yr
from orders
group by customer_id
union all
select t.customer_id, t.min_year, t.max_year, DATEADD(YEAR, 1, t.yr)
from t
where DATEADD(YEAR, 1, t.yr) <= max_year
),
t1 (customer_id, order_year, total_purchase) as (
select customer_id,
       CONVERT(DATETIME, CONVERT(VARCHAR(4), order_date, 120) + '-01-01') as order_year,
       sum(price) as total_purchase
from orders
group by customer_id, CONVERT(DATETIME, CONVERT(VARCHAR(4), order_date, 120) + '-01-01')
),
t2 (customer_id, yr, total_purchase, diff) as (
select t.customer_id,
       t.yr,
       coalesce(t1.total_purchase, 0) as total_purchase,
       coalesce(t1.total_purchase, 0)
       -
       lag(coalesce(t1.total_purchase, 0)) over (partition by t.customer_id order by t.yr) as diff
from t
     left outer join t1 on (t1.customer_id = t.customer_id and t1.order_year = t.yr)
)
select distinct x.customer_id
from t2 x
where not exists (select null from t2 y where y.customer_id = x.customer_id and y.diff <= 0)
;


# MySQL
# Write your MySQL query statement below
with recursive t (customer_id, min_year, max_year, yr) as (
select customer_id,
       min(str_to_date(DATE_FORMAT(order_date, '%Y-01-01'), '%Y-%m-%d')) as min_year,
       max(str_to_date(DATE_FORMAT(order_date, '%Y-01-01'), '%Y-%m-%d')) as max_year,
       min(str_to_date(DATE_FORMAT(order_date, '%Y-01-01'), '%Y-%m-%d')) as yr
from orders
group by customer_id
union all
select t.customer_id, t.min_year, t.max_year, t.yr + INTERVAL 1 YEAR
from t
where t.yr + INTERVAL 1 YEAR <= max_year
),
t1 (customer_id, order_year, total_purchase) as (
select customer_id,
       str_to_date(DATE_FORMAT(order_date, '%Y-01-01'), '%Y-%m-%d') as order_year,
       sum(price) as total_purchase
from orders
group by customer_id, str_to_date(DATE_FORMAT(order_date, '%Y-01-01'), '%Y-%m-%d')
),
t2 (customer_id, yr, total_purchase, diff) as (
select t.customer_id,
       t.yr,
       coalesce(t1.total_purchase, 0) as total_purchase,
       coalesce(t1.total_purchase, 0)
       -
       lag(coalesce(t1.total_purchase, 0)) over (partition by t.customer_id order by t.yr) as diff
from t
     left outer join t1 on (t1.customer_id = t.customer_id and t1.order_year = t.yr)
)
select distinct x.customer_id
from t2 x
where not exists (select null from t2 y where y.customer_id = x.customer_id and y.diff <= 0)
;

