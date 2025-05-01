-- Oracle
/* Write your PL/SQL query statement below */
select to_char(order_date, 'yyyy-mm') as month,
       count(distinct order_id) as order_count,
       count(distinct customer_id) as customer_count
from orders
where invoice > 20
group by to_char(order_date, 'yyyy-mm')
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select convert(varchar(7), order_date, 120) as month,
       count(distinct order_id) as order_count,
       count(distinct customer_id) as customer_count
from orders
where invoice > 20
group by convert(varchar(7), order_date, 120)
;


# MySQL
# Write your MySQL query statement below
select date_format(order_date, '%Y-%m') as month,
       count(distinct order_id) as order_count,
       count(distinct customer_id) as customer_count
from orders
where invoice > 20
group by date_format(order_date, '%Y-%m')
;


# Pandas
import pandas as pd

def unique_orders_and_customers(orders: pd.DataFrame) -> pd.DataFrame:
    orders['order_date'] = orders['order_date'].dt.strftime('%Y-%m')
    return (  orders[orders['invoice'] > 20]
              .groupby('order_date',as_index=False)[['order_id','customer_id']]
              .nunique()
              .rename(columns={'order_date':'month', 'order_id':'order_count', 'customer_id':'customer_count'})
           )

