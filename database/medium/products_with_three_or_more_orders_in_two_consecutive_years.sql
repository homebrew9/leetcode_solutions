-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select product_id,
       trunc(purchase_date, 'yyyy') as purchase_year,
       count(*) as cnt
from orders
group by product_id, trunc(purchase_date, 'yyyy')
)
select distinct t.product_id --, t.purchase_year, t.cnt, t1.cnt
from t
     inner join t t1
     on (t1.product_id = t.product_id and t1.purchase_year = trunc(add_months(t.purchase_year,12),'yyyy'))
where t.cnt >= 3
and t1.cnt >= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select product_id,
       date_trunc('year', purchase_date) as purchase_year,
       count(*) as cnt
from orders
group by product_id, date_trunc('year', purchase_date)
)
select distinct t.product_id
from t
     inner join t t1
     on (
            t1.product_id = t.product_id
            and
            t1.purchase_year =  t.purchase_year + interval '1 year'
        )
where t.cnt >= 3
and t1.cnt >= 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select product_id,
       CONVERT(DATETIME, CONVERT(VARCHAR(4), purchase_date, 120) + '-01-01') as purchase_year,
       count(*) as cnt
from orders
group by product_id,
         CONVERT(DATETIME, CONVERT(VARCHAR(4), purchase_date, 120) + '-01-01')
)
select distinct t.product_id
from t
     inner join t t1
     on (
            t1.product_id = t.product_id
            and
            t1.purchase_year = DATEADD(YEAR, 1, t.purchase_year)
        )
where t.cnt >= 3
and t1.cnt >= 3
;


# MySQL
# Write your MySQL query statement below
with t as (
select product_id,
       str_to_date(DATE_FORMAT(purchase_date, '%Y-01-01'), '%Y-%m-%d') as purchase_year,
       count(*) as cnt
from orders
group by product_id,
         str_to_date(DATE_FORMAT(purchase_date, '%Y-01-01'), '%Y-%m-%d')
)
select distinct t.product_id
from t
     inner join t t1
     on (
            t1.product_id = t.product_id
            and
            t1.purchase_year =  t.purchase_year + interval 1 year
        )
where t.cnt >= 3
and t1.cnt >= 3
;


# Pandas

