-- Oracle
/* Write your PL/SQL query statement below */
select product_id
  from products
 where low_fats = 'Y'
   and recyclable = 'Y'
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select product_id
  from products
 where low_fats = 'Y'
   and recyclable = 'Y'
;


-- SQL Server
/* Write your T-SQL query statement below */
select product_id
  from products
 where low_fats = 'Y'
   and recyclable = 'Y'
;


# MySQL
# Write your MySQL query statement below
select product_id
from products
where low_fats = 'Y'
and recyclable = 'Y'
;


# Pandas
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.query('low_fats == "Y" & recyclable == "Y"')[['product_id']]

