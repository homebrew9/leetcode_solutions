-- Oracle


-- PostgreSQL


-- SQL Server


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

