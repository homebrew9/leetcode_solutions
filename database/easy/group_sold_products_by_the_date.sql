-- Oracle
/* Write your PL/SQL query statement below */
select to_char(sell_date,'YYYY-MM-DD') as "sell_date",
       count(*) as "num_sold",
       listagg(product, ',') within group (order by product) as "products"
from (select distinct sell_date, product from activities) t
group by to_char(sell_date,'YYYY-MM-DD')
order by to_char(sell_date,'YYYY-MM-DD')
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (sell_date, product) as (
    select distinct sell_date, product
      from activities
)
select sell_date, count(*) as num_sold,
       string_agg(product, ',' order by product) as products
  from t
 group by sell_date
 order by sell_date
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (sell_date, product) as (
    select distinct sell_date, product
      from activities
)
select sell_date, count(*) as num_sold,
       string_agg(product, ',') within group (order by product) as products
  from t
 group by sell_date
 order by sell_date
;


# MySQL
# Write your MySQL query statement below
with t (sell_date, product) as (
    select distinct sell_date, product
      from activities
)
select sell_date, count(*) as num_sold,
       group_concat(product order by product separator ',') as products
  from t
 group by sell_date
 order by sell_date
;


# Pandas
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.sort_values(by=['sell_date','product']).drop_duplicates()
    return pd.merge(
        activities.groupby(by=['sell_date'], as_index=False).agg(num_sold=('sell_date','count')),
        activities.groupby(by=['sell_date'], as_index=False).agg(products=('product', ','.join)),
        how = 'inner',
        on = 'sell_date'
    ).sort_values('sell_date')

