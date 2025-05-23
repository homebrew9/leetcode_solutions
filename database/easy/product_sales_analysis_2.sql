-- Oracle
/* Write your PL/SQL query statement below */
select p.product_id, sum(s.quantity) as total_quantity
  from product p
       inner join sales s on (s.product_id = p.product_id)
 group by p.product_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.product_id, sum(s.quantity) as total_quantity
  from product p
       inner join sales s on (s.product_id = p.product_id)
 group by p.product_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select product_id, sum(quantity) as total_quantity
  from sales
 group by product_id
;


# MySQL
# Write your MySQL query statement below
select product_id, sum(quantity) as total_quantity
  from sales
 group by product_id
;


# Pandas
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return ( sales
            .groupby('product_id', as_index=False)['quantity']
            .sum()
            .rename(columns={'quantity': 'total_quantity'})
           )

