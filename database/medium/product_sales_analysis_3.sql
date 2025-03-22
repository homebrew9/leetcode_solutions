-- Oracle
/* Write your PL/SQL query statement below */
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


# MySQL
# Write your MySQL query statement below
with t (product_id, year, quantity, price, min_year) as (
select product_id, year, quantity, price,
       min(year) over (partition by product_id) as min_year
from sales
)
select product_id, year as first_year, quantity, price
from t
where year = min_year
;


# Pandas
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.groupby('product_id', as_index=0)['year'].min()
    return ( sales
            .merge(product, how='inner', on='product_id')
            .merge(df, how='inner', on=['product_id', 'year'])[['product_id', 'year', 'quantity', 'price']]
            .rename(columns={'year': 'first_year'})
           )

