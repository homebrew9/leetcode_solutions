-- Oracle
/* Write your PL/SQL query statement below */
with t (order_id, product_id, quantity, avg_per_order_id, max_per_order_id) as (
select order_id, product_id, quantity,
       avg(quantity) over (partition by order_id) as avg_per_order_id,
       max(quantity) over (partition by order_id) as max_per_order_id
from OrdersDetails
),
t1 (order_id, product_id, quantity, avg_per_order_id, max_per_order_id, max_avg_of_all_order_id) as (
select order_id, product_id, quantity, avg_per_order_id, max_per_order_id,
       max(avg_per_order_id) over () as max_avg_of_all_order_id
from t
)
select distinct order_id
from t1
where max_per_order_id > max_avg_of_all_order_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (order_id, product_id, quantity, avg_per_order_id, max_per_order_id) as (
select order_id, product_id, quantity,
       avg(quantity) over (partition by order_id) as avg_per_order_id,
       max(quantity) over (partition by order_id) as max_per_order_id
from OrdersDetails
),
t1 (order_id, product_id, quantity, avg_per_order_id, max_per_order_id, max_avg_of_all_order_id) as (
select order_id, product_id, quantity, avg_per_order_id, max_per_order_id,
       max(avg_per_order_id) over () as max_avg_of_all_order_id
from t
)
select distinct order_id
from t1
where max_per_order_id > max_avg_of_all_order_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (order_id, product_id, quantity, avg_per_order_id, max_per_order_id) as (
select order_id, product_id, quantity,
       avg(quantity) over (partition by order_id) as avg_per_order_id,
       max(quantity) over (partition by order_id) as max_per_order_id
from OrdersDetails
),
t1 (order_id, product_id, quantity, avg_per_order_id, max_per_order_id, max_avg_of_all_order_id) as (
select order_id, product_id, quantity, avg_per_order_id, max_per_order_id,
       max(avg_per_order_id) over () as max_avg_of_all_order_id
from t
)
select distinct order_id
from t1
where max_per_order_id > max_avg_of_all_order_id
;


# MySQL
# Write your MySQL query statement below
with t (order_id, product_id, quantity, avg_per_order_id, max_per_order_id) as (
select order_id, product_id, quantity,
       avg(quantity) over (partition by order_id) as avg_per_order_id,
       max(quantity) over (partition by order_id) as max_per_order_id
from OrdersDetails
),
t1 (order_id, product_id, quantity, avg_per_order_id, max_per_order_id, max_avg_of_all_order_id) as (
select order_id, product_id, quantity, avg_per_order_id, max_per_order_id,
       max(avg_per_order_id) over () as max_avg_of_all_order_id
from t
)
select distinct order_id
from t1
where max_per_order_id > max_avg_of_all_order_id
;


# Pandas
import pandas as pd

def orders_above_average(orders_details: pd.DataFrame) -> pd.DataFrame:
    orders_details.sort_values(['order_id','product_id','quantity'], inplace=True)
    df = orders_details.assign(max_qty=orders_details.groupby('order_id')['quantity'].transform('max'),
                               avg_qty=orders_details.groupby('order_id')['quantity'].transform('mean')
                              )
    df = df.assign(max_of_all_avg_qty=df['avg_qty'].max())
    return df[df['max_qty'] > df['max_of_all_avg_qty']][['order_id']].drop_duplicates()

