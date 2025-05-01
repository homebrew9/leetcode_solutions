-- Oracle
/* Write your PL/SQL query statement below */
select product_id, name
  from products
 where regexp_like(name, '(^|\D)\d{3}(\D|$)')
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select product_id, name
  from products
 where regexp_like(name, '(^|\D)\d{3}(\D|$)')
;


-- SQL Server
/* Write your T-SQL query statement below */
select product_id, name
from products
where name like '%[0-9][0-9][0-9]%'
and name not like '%[0-9][0-9][0-9][0-9]%'
order by product_id
;


# MySQL
# Write your MySQL query statement below
select product_id, name
  from products
 where regexp_like(name, '(^|[^[:digit:]])[[:digit:]]{3}([^[:digit:]]|$)')
;


# Pandas
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[('X'+products['name']+'X').str.contains(r'\D\d{3}\D')]

