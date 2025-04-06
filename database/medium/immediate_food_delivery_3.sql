-- Oracle
/* Write your PL/SQL query statement below */
select to_char(order_date, 'YYYY-MM-DD') as order_date,
       round(
              sum(case order_date when customer_pref_delivery_date then 1 else 0 end)
              /
              count(*)
              *
              100,
              2
            ) as immediate_percentage
from delivery
group by order_date
order by order_date
;


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
import pandas as pd

def immediate_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['immediate'] = delivery['order_date'] == delivery['customer_pref_delivery_date']
    df = ( delivery
          .groupby('order_date', as_index=False)
          .agg(imm_cnt=('immediate','sum'), total_cnt=('delivery_id','count'))
         )
    df['immediate_percentage'] = round(df['imm_cnt']/df['total_cnt']*100, 2)
    return df[['order_date','immediate_percentage']].sort_values('order_date')

