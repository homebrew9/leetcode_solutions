-- Oracle
/* Write your PL/SQL query statement below */
select *
from products
unpivot (
    price
    for store in (
        store1 as 'store1',
        store2 as 'store2',
        store3 as 'store3'
    )
)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- PostgreSQL does not have an UNPIVOT operator.
-- We can use the "values" clause like a table, and simulate the unpivot.
select p.product_id, t.store, t.price
  from products p
       cross join lateral (
           values
               ('store1', p.store1),
               ('store2', p.store2),
               ('store3', p.store3)
       ) as t (store, price)
 where t.price is not null
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (product_id, store, price) as (
    select product_id, 'store1', store1 from products union all
    select product_id, 'store2', store2 from products union all
    select product_id, 'store3', store3 from products
)
select product_id, store, price
  from t
 where price is not null
;


# MySQL
# Write your MySQL query statement below
with t (product_id, store, price) as (
    select product_id, 'store1', store1 from products union all
    select product_id, 'store2', store2 from products union all
    select product_id, 'store3', store3 from products
)
select product_id, store, price
  from t
 where price is not null
;


# Pandas
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return products.melt(id_vars='product_id', var_name='store', value_name='price').dropna()

