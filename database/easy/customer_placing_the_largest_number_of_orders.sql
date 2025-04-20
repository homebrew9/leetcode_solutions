-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select customer_number, count(*) as order_count
      from orders
     group by customer_number
)
select t.customer_number
  from t
 where t.order_count = (select max(order_count) from t)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (customer_number, order_count) as (
    select customer_number, count(*) as order_count
      from orders
     group by customer_number
)
select customer_number
  from t
 where order_count = (select max(order_count) from t)
;


-- SQL Server
/* Write your T-SQL query statement below */
--
with t as (
    select customer_number, count(*) as cnt
    from orders
    group by customer_number
),
t1 as (
    select customer_number, cnt, dense_rank() over (order by cnt desc) as drnk
    from t
)
select customer_number
from t1
where drnk = 1
;


# MySQL
# Write your MySQL query statement below
#
# Follow up: What if more than one customer has the largest number of orders,
#            can you find all the customer_number in this case?
# Answer   : The query below will fetch all such customers in that case.
#
with t as (
select customer_number, count(*) as order_count
from orders
group by customer_number
)
select customer_number
from t
where order_count = (select max(order_count) from t)
;


# Pandas
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()

