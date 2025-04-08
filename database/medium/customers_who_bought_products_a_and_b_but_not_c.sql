-- Oracle
/* Write your PL/SQL query statement below */
with t (customer_id, customer_name, products) as (
    select c.customer_id,
           c.customer_name,
           listagg(o.product_name,',') within group (order by o.product_name) as products
      from customers c
           inner join orders o on (o.customer_id = c.customer_id)
     group by c.customer_id, c.customer_name
)
select customer_id, customer_name
  from t
 where products like '%A%'
   and products like '%B%'
   and products not like '%C%'
 order by customer_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select c.customer_id, c.customer_name
from customers c
where exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'A')
and exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'B')
and not exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'C')
order by c.customer_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select c.customer_id, c.customer_name
from customers c
where exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'A')
and exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'B')
and not exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'C')
order by c.customer_id
;


# MySQL
# Write your MySQL query statement below
select c.customer_id, c.customer_name
from customers c
where exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'A')
and exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'B')
and not exists (select null from orders o where o.customer_id = c.customer_id and o.product_name = 'C')
order by c.customer_id
;


# Pandas
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return ( customers[['customer_id','customer_name']]
            .merge(pd.DataFrame(data={'product_name':['A','B','C']}), how='cross')
            .merge(orders, how='left', on=['customer_id','product_name'])
            .fillna(-1)
            .pivot_table(index=['customer_id','customer_name'], columns='product_name', values='order_id')
            .reset_index()
            .query('A != -1 & B != -1 & C == -1')[['customer_id','customer_name']]
           )

