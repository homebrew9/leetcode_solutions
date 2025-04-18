-- Oracle
/* Write your PL/SQL query statement below */
select s.seller_name
  from seller s
 where not exists (select null
                     from orders o
                    where o.seller_id = s.seller_id
                      and to_char(sale_date, 'yyyy') = '2020'
                  )
order by s.seller_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select seller_name
from seller
where seller_id not in (
    select seller_id
    from orders
    where date_part('year', sale_date) = 2020
)
order by seller_name
;


-- SQL Server


# MySQL
# Write your MySQL query statement below
select seller_name
from seller
where seller_id not in (
    select seller_id
    from orders
    where date_format(sale_date, '%Y') = '2020'
)
order by seller_name
;


# Pandas
import pandas as pd

def sellers_with_no_sales(customer: pd.DataFrame, orders: pd.DataFrame, seller: pd.DataFrame) -> pd.DataFrame:
    sellers_in_2020 = orders[orders['sale_date'].dt.strftime('%Y')=='2020']['seller_id']
    return seller[~seller['seller_id'].isin(sellers_in_2020)][['seller_name']].sort_values('seller_name')

