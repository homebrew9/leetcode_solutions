-- Oracle
/* Write your PL/SQL query statement below */
select p.product_name, sum(unit) as unit
  from orders o
       inner join products p on (p.product_id = o.product_id)
 where to_char(o.order_date, 'YYYY-MM') = '2020-02'
 group by p.product_name, p.product_id
having sum(unit) >= 100
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.product_name, sum(unit) as unit
  from orders o
       inner join products p on (p.product_id = o.product_id)
 where to_char(o.order_date, 'YYYY-MM') = '2020-02'
 group by p.product_name, p.product_id
having sum(unit) >= 100
;


-- SQL Server
/* Write your T-SQL query statement below */
select p.product_name, sum(unit) as unit
  from orders o
       inner join products p on (p.product_id = o.product_id)
 where YEAR(o.order_date) = 2020
   and MONTH(o.order_date) = 2
 group by p.product_name, p.product_id
having sum(unit) >= 100
;


# MySQL
# Write your MySQL query statement below
select p.product_name, sum(unit) as unit
  from orders o
       inner join products p on (p.product_id = o.product_id)
 where YEAR(o.order_date) = 2020
   and MONTH(o.order_date) = 2
 group by p.product_name, p.product_id
having sum(unit) >= 100
;


# Pandas
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return ( orders[orders['order_date'].dt.strftime('%Y-%m') == '2020-02']
            .groupby('product_id', as_index=0)['unit']
            .sum()
            .query('unit >= 100')
            .merge(products, how='inner', on='product_id')[['product_name', 'unit']]
           )

