-- Oracle
/* Write your PL/SQL query statement below */
select round( sum(case when customer_pref_delivery_date = order_date then 1 else 0 end)
              /
              count(*) * 100
             , 2
            ) as immediate_percentage
  from delivery
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select round((x.immediate / y.total * 100)::numeric, 2) as immediate_percentage
from (select count(*)::float as immediate from delivery where order_date = customer_pref_delivery_date) x
     cross join
     (select count(*)::float as total from delivery) y
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_rows (cnt) as (
    select count(*) as cnt
      from delivery
),
t_immediate (cnt) as (
    select count(*) as cnt
      from delivery
     where order_date = customer_pref_delivery_date
)
select round(convert(float, ti.cnt) / convert(float, tr.cnt) * 100, 2) as "immediate_percentage"
from t_immediate ti
     cross join t_rows tr
;


# MySQL
# Write your MySQL query statement below
select round(x.immediate / y.total * 100, 2) as immediate_percentage
from (select count(*) as immediate from delivery where order_date = customer_pref_delivery_date) x
     cross join
     (select count(*) as total from delivery) y
;


# Pandas
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    pct = round(len(delivery[delivery['order_date']==delivery['customer_pref_delivery_date']])/len(delivery)*100,2)
    return pd.DataFrame(data={'immediate_percentage': [pct]})

