-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
select order_date,
       round(
              sum(case order_date when customer_pref_delivery_date then 1 else 0 end)::numeric
              /
              count(*)::numeric
              *
              100,
             2
            ) as immediate_percentage
from delivery
group by order_date
order by order_date
;


-- SQL Server


# MySQL
# Write your MySQL query statement below
select order_date,
       round(sum(case order_date when customer_pref_delivery_date then 1 else 0 end)/count(*)*100, 2) as immediate_percentage
from delivery
group by order_date
order by order_date
;


# Pandas

