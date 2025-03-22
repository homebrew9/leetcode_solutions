-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       purchase_date - lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       purchase_date - lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       DATEDIFF( DAY,
                 lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id),
                 purchase_date
               ) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


# MySQL
# Write your MySQL query statement below
with t as (
select purchase_id, user_id, purchase_date,
       lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as prev_purchase_dt,
       #purchase_date - lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id) as diff
       DATEDIFF(purchase_date , lag(purchase_date) over (partition by user_id order by purchase_date, purchase_id)) as diff
from purchases
)
select distinct user_id
from t
where diff <= 7
order by user_id
;


# Pandas

