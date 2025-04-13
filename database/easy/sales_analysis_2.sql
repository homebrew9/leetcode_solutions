-- Oracle
/* Write your PL/SQL query statement below */
with t (buyer_id, product_name) as (
    select s.buyer_id, p.product_name
      from sales s
           inner join product p on (p.product_id = s.product_id)
)
select distinct x.buyer_id
  from t x
 where x.product_name = 'S8'
   and not exists (select null
                     from t y
                    where y.buyer_id = x.buyer_id
                      and y.product_name = 'iPhone'
                  )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (buyer_id, product_name) as (
    select s.buyer_id, p.product_name
      from sales s
           inner join product p on (p.product_id = s.product_id)
)
select distinct x.buyer_id
  from t x
 where x.product_name = 'S8'
   and not exists (select null
                     from t y
                    where y.buyer_id = x.buyer_id
                      and y.product_name = 'iPhone'
                  )
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (buyer_id, product_name) as (
    select distinct s.buyer_id, p.product_name
      from sales s
           inner join product p on (p.product_id = s.product_id)
)
select x.buyer_id
  from t x
 where x.product_name = 'S8'
   and not exists (select null
                     from t y
                    where y.buyer_id = x.buyer_id
                      and y.product_name = 'iPhone'
                  )
;


# MySQL
# Write your MySQL query statement below
with t (buyer_id, product_name) as (
    select s.buyer_id, p.product_name
      from sales s
           inner join product p on (p.product_id = s.product_id)
)
select distinct x.buyer_id
  from t x
 where x.product_name = 'S8'
   and not exists (select null
                     from t y
                    where y.buyer_id = x.buyer_id
                      and y.product_name = 'iPhone'
                  )
;


# Pandas
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, how='inner', on='product_id')
    iphone_buyers = df[df['product_name'] == 'iPhone']['buyer_id']
    return df[(df['product_name'] == 'S8') & (~df['buyer_id'].isin(iphone_buyers))][['buyer_id']].drop_duplicates()

