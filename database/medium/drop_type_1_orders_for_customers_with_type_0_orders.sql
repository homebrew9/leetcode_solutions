-- Oracle
/* Write your PL/SQL query statement below */
with t (order_id, customer_id, order_type, has_type0_order) as (
select x.order_id, x.customer_id, x.order_type,
       (select y.order_type
          from orders y
         where y.customer_id = x.customer_id
           and y.order_type = 0
           and rownum = 1
       ) as has_type0_order
from orders x
)
select order_id, customer_id, order_type
from t
where has_type0_order is null or order_type = has_type0_order
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (order_id, customer_id, order_type, has_type0_order) as (
select x.order_id, x.customer_id, x.order_type,
       (select y.order_type
          from orders y
         where y.customer_id = x.customer_id
           and y.order_type = 0
         limit 1
       ) as has_type0_order
from orders x
)
select order_id, customer_id, order_type
from t
where has_type0_order is null or order_type = has_type0_order
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (order_id, customer_id, order_type, has_type0_order) as (
select x.order_id, x.customer_id, x.order_type,
       (select top 1 y.order_type
          from orders y
         where y.customer_id = x.customer_id
           and y.order_type = 0
       ) as has_type0_order
from orders x
)
select order_id, customer_id, order_type
from t
where has_type0_order is null or order_type = has_type0_order
;


# MySQL
# Write your MySQL query statement below
with t (order_id, customer_id, order_type, has_type0_order) as (
select x.order_id, x.customer_id, x.order_type,
       (select y.order_type
          from orders y
         where y.customer_id = x.customer_id
           and y.order_type = 0
         limit 1
       ) as has_type0_order
from orders x
)
select order_id, customer_id, order_type
from t
where has_type0_order is null or order_type = has_type0_order
;


# Pandas
import pandas as pd

def drop_specific_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders[orders['order_type'] == 0][['customer_id']].drop_duplicates()
    df['has_type0_orders'] = 1
    return (  orders.merge(df, how='left', on='customer_id')
                    .query('has_type0_orders.isna() or order_type == 0')[['order_id','customer_id','order_type']]
           )

