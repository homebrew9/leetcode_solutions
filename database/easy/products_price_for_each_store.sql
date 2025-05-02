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
-- The LC setup does not have the tablefunc module installed, hence the crosstab queries below fail in LC.
-- But they can be tested in other PostgreSQL installations that do have the tablefunc module.
-- If the tablefunc module has been installed, then we can use crosstab function.
-- Pivot the data so that stores are displayed as columns, indexed by product_id
-- Documentation of functions in the tablefunc module: normal_rand, crosstab, crosstabN, connectby etc.
-- https://www.postgresql.org/docs/current/tablefunc.html
--
select *
  from crosstab (
      'select product_id, store, amount from products order by product_id',
	  'select distinct store from products order by store'
  ) as ct(product_id int, "store1" int, "store2" int, "store3" int, "store4" int)
;
-- The single query version of crosstab works as well - but we have to return all combinations
-- of (product_id, store) otherwise the amounts are displayed under incorrect stores.
--
select *
  from crosstab
  (
        'with t as (
            select x.product_id, y.store
              from (select distinct product_id from products) x
                    cross join
                   (select distinct store from products) y
        ),
        t1 as (
            select product_id, store, sum(amount) as amount
              from products
             group by product_id, store
        )
        select t.product_id, t.store, t1.amount::float8
          from t
               left outer join t1 on (t1.product_id = t.product_id and t1.store = t.store)
         order by t.product_id, t.store'
  )
  as ct(product_id int, "store1" float8, "store2" float8, "store3" float8, "store4" float8)
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

