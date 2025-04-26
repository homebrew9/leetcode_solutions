-- Oracle
/* Write your PL/SQL query statement below */
with t (seller_id, total_price) as (
    select seller_id, sum(price) as total_price
      from sales
     group by seller_id
),
t1 (seller_id, total_price, max_total_price) as (
    select seller_id, total_price,
           max(total_price) over () as max_total_price
      from t
)
select seller_id as "seller_id"
  from t1
 where total_price = max_total_price
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (seller_id, total_price) as (
    select seller_id, sum(price) as total_price
      from sales
     group by seller_id
),
t1 (seller_id, total_price, max_total_price) as (
    select seller_id, total_price,
           max(total_price) over () as max_total_price
      from t
)
select seller_id
  from t1
 where total_price = max_total_price
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (seller_id, total_price) as (
    select seller_id, sum(price) as total_price
      from sales
     group by seller_id
),
t1 (seller_id, total_price, max_total_price) as (
    select seller_id, total_price,
           max(total_price) over () as max_total_price
      from t
)
select seller_id as "seller_id"
  from t1
 where total_price = max_total_price
;


# MySQL
# Write your MySQL query statement below
with t (seller_id, total_price) as (
    select seller_id, sum(price) as total_price
      from sales
     group by seller_id
),
t1 (seller_id, total_price, max_total_price) as (
    select seller_id, total_price,
           max(total_price) over () as max_total_price
      from t
)
select seller_id as "seller_id"
  from t1
 where total_price = max_total_price
;


# Pandas
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('seller_id',as_index=False)['price'].sum()
    return df[df['price'] == max(df['price'])][['seller_id']]

