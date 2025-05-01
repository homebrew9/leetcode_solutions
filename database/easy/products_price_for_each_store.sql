-- Oracle


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
-- Looks like pivoting is complex in MySQL. See links:
-- https://stackoverflow.com/questions/67021424/using-pivot-to-join-tables-using-mysql-8-version
-- https://mariadb.com/kb/en/pivoting-in-mariadb/
-- https://mysql.rjweb.org/doc.php/pivot
-- We use our trusty old "max decode" trick.

select product_id,
       max(case when store = 'store1' then price end) as store1,
       max(case when store = 'store2' then price end) as store2,
       max(case when store = 'store3' then price end) as store3
  from products
 group by product_id
;


# Pandas
import pandas as pd

def products_price(products: pd.DataFrame) -> pd.DataFrame:
    return products.pivot(values='price', index='product_id', columns='store').reset_index()

