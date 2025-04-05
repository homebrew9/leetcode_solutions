-- Oracle
/* Write your PL/SQL query statement below */
with t (product_id, product_name, order_id, order_date, drnk) as (
    select o.product_id, p.product_name, o.order_id, o.order_date,
           dense_rank() over (partition by o.product_id order by o.order_date desc) as drnk
      from orders o
           inner join products p on (p.product_id = o.product_id)
)
select product_name, product_id, order_id, to_char(order_date, 'YYYY-MM-DD') as order_date
  from t
 where drnk = 1
 order by product_name, product_id, order_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (product_name, product_id, order_id, order_date, drnk) as (
select p.product_name, p.product_id, o.order_id, o.order_date,
       dense_rank() over (partition by p.product_id order by o.order_date desc) as drnk
from orders o
     inner join products p on (p.product_id = o.product_id)
)
select product_name, product_id, order_id, order_date
from t
where drnk = 1
order by product_name, product_id, order_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (product_name, product_id, order_id, order_date, drnk) as (
select p.product_name, p.product_id, o.order_id, o.order_date,
       dense_rank() over (partition by p.product_id order by o.order_date desc) as drnk
from orders o
     inner join products p on (p.product_id = o.product_id)
)
select product_name, product_id, order_id, order_date
from t
where drnk = 1
order by product_name, product_id, order_id
;


# MySQL
# Write your MySQL query statement below
with t (product_name, product_id, order_id, order_date, drnk) as (
select p.product_name, p.product_id, o.order_id, o.order_date,
       dense_rank() over (partition by p.product_id order by o.order_date desc) as drnk
from orders o
     inner join products p on (p.product_id = o.product_id)
)
select product_name, product_id, order_id, order_date
from t
where drnk = 1
order by product_name, product_id, order_id
;


# Pandas
import pandas as pd

def most_recent_orders(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    return ( orders
            .assign(drnk=orders.groupby('product_id',as_index=0)['order_date'].rank(method='dense', ascending=False))
            .query('drnk==1')
            .merge(products, how='inner', on='product_id')[['product_name','product_id','order_id','order_date']]
            .sort_values(by=['product_name','product_id','order_id'])
           )

