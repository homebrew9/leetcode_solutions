-- Oracle
/* Write your PL/SQL query statement below */
select p.product_name, s.year, s.price
from sales s
     inner join product p on (p.product_id = s.product_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.product_name, s.year, s.price
from sales s
     inner join product p on (p.product_id = s.product_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
select p.product_name, s.year, s.price
from sales s
     inner join product p on (p.product_id = s.product_id)
;


# MySQL
# Write your MySQL query statement below
select p.product_name, s.year, s.price
from sales s
     inner join product p on (p.product_id = s.product_id)
;


# Pandas
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales.merge(product, how='inner', on='product_id')[['product_name','year','price']]

