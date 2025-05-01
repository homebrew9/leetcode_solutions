-- Oracle
/* Write your PL/SQL query statement below */
select *
from products
pivot (max(price)
       for (store) in ('store1' as store1, 'store2' as store2, 'store3' as store3)
      )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- AWS Aurora PostgreSQL has PIVOT/UNPIVOT operators, which are not in core PostgreSQL.
-- "crosstab" function is in core PostgreSQL, but it requires installation of "tablefunc" module.
-- So we use our plain old "max decode" trick!
select product_id,
       max(case when store = 'store1' then price end) as store1,
       max(case when store = 'store2' then price end) as store2,
       max(case when store = 'store3' then price end) as store3
  from products
 group by product_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select product_id, store1, store2, store3
from products as source_set
pivot
(
    max(price)
    for [store] in ([store1], [store2], [store3])
) as pivot_set
;


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

