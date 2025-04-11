-- Oracle
/* Write your PL/SQL query statement below */
with t (customer_id, product_id, order_count) as (
    select customer_id, product_id, count(*) as order_count
      from orders
     group by customer_id, product_id
),
t1 (customer_id, product_id, order_count, drnk) as (
    select customer_id, product_id, order_count,
           dense_rank() over (partition by customer_id order by order_count desc) as drnk
      from t
)
select t1.customer_id, t1.product_id, p.product_name
  from t1
       inner join products p on (p.product_id = t1.product_id)
 where t1.drnk = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (customer_id, product_id, order_frequency) as (
select customer_id, product_id, count(*) as order_frequency
from orders
group by customer_id, product_id
),
t1 (customer_id, product_id, order_frequency, rnk) as (
select customer_id, product_id, order_frequency,
       rank() over (partition by customer_id order by order_frequency desc) as rnk
from t
)
select t1.customer_id, t1.product_id, p.product_name
from t1 inner join products p on (p.product_id = t1.product_id)
where t1.rnk = 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (customer_id, product_id, order_frequency) as (
select customer_id, product_id, count(*) as order_frequency
from orders
group by customer_id, product_id
),
t1 (customer_id, product_id, order_frequency, rnk) as (
select customer_id, product_id, order_frequency,
       rank() over (partition by customer_id order by order_frequency desc) as rnk
from t
)
select t1.customer_id, t1.product_id, p.product_name
from t1 inner join products p on (p.product_id = t1.product_id)
where t1.rnk = 1
;


# MySQL
# Write your MySQL query statement below
with t (customer_id, product_id, order_frequency) as (
select customer_id, product_id, count(*) as order_frequency
from orders
group by customer_id, product_id
),
t1 (customer_id, product_id, order_frequency, rnk) as (
select customer_id, product_id, order_frequency,
       rank() over (partition by customer_id order by order_frequency desc) as rnk
from t
)
select t1.customer_id, t1.product_id, p.product_name
from t1 inner join products p on (p.product_id = t1.product_id)
where t1.rnk = 1
;


# Pandas
import pandas as pd

def most_frequently_products(customers: pd.DataFrame, orders: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby(['customer_id','product_id'],as_index=False)['order_id'].count()
    df = df.assign(rnk=df.groupby(['customer_id'])['order_id'].rank(method='dense',ascending=0)).query('rnk==1')
    return df.merge(products, how='inner', on='product_id')[['customer_id','product_id','product_name']]

