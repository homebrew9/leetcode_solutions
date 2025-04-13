-- Oracle
/* Write your PL/SQL query statement below */
select p.name,
       coalesce(sum(i.rest), 0) as rest,
       coalesce(sum(i.paid), 0) as paid,
       coalesce(sum(i.canceled), 0) as canceled,
       coalesce(sum(i.refunded), 0) as refunded
from product p
     left join invoice i on (i.product_id = p.product_id)
group by p.name
order by 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.name,
       coalesce(sum(i.rest), 0) as rest,
       coalesce(sum(i.paid), 0) as paid,
       coalesce(sum(i.canceled), 0) as canceled,
       coalesce(sum(i.refunded), 0) as refunded
from product p
     left join invoice i on (i.product_id = p.product_id)
group by p.name
order by 1
;


-- SQL Server
/* Write your T-SQL query statement below */
select p.name,
       coalesce(sum(i.rest), 0) as rest,
       coalesce(sum(i.paid), 0) as paid,
       coalesce(sum(i.canceled), 0) as canceled,
       coalesce(sum(i.refunded), 0) as refunded
from product p
     left join invoice i on (i.product_id = p.product_id)
group by p.name
order by 1
;


# MySQL
# Write your MySQL query statement below
select p.name,
       coalesce(sum(i.rest), 0) as rest,
       coalesce(sum(i.paid), 0) as paid,
       coalesce(sum(i.canceled), 0) as canceled,
       coalesce(sum(i.refunded), 0) as refunded
from product p
     left join invoice i on (i.product_id = p.product_id)
group by p.name
order by 1
;


# Pandas
import pandas as pd

def analyze_products(product: pd.DataFrame, invoice: pd.DataFrame) -> pd.DataFrame:
    df = (  invoice.groupby('product_id', as_index=False)[['rest','paid','canceled','refunded']]
                   .sum()
         )
    return (  product.merge(df, how='left', on='product_id')
                     .fillna(0)[['name','rest','paid','canceled','refunded']]
                     .sort_values('name')
           )

