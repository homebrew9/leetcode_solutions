-- Oracle
/* Write your PL/SQL query statement below */
select product_id, product_name, description
  from products
 where regexp_like(description, '(^|\s)SN(\d){4}-(\d){4}(\s|$)')
 order by product_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select product_id, product_name, description
  from products
 where regexp_like(description, '(^|\s)SN(\d){4}-(\d){4}(\s|$)')
 order by product_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select product_id, product_name, description
from products
where description like 'SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]%'
or description like '%SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]'
or description like '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] %'
order by product_id
;


# MySQL
# Write your MySQL query statement below
select product_id, product_name, description
  from products
 where regexp_like(description, '(^| )SN[0-9]{4}-[0-9]{4}( |$)')
 order by product_id
;


# Pandas
import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    return ( products[products['description'].str.contains(r'(^|\s)SN\d{4}-\d{4}(\s|$)', regex=True)]
            .sort_values('product_id')
           )

