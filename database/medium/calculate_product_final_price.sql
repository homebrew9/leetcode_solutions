-- Oracle
/* Write your PL/SQL query statement below */
select p.product_id, p.price * (1 - coalesce(d.discount, 0)/100) as final_price, p.category
  from products p
       left outer join discounts d on (d.category = p.category)
 order by p.product_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.product_id, p.price * (1 - coalesce(d.discount::numeric, 0)/100) as final_price, p.category
  from products p
       left outer join discounts d on (d.category = p.category)
 order by p.product_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select p.product_id,
       p.price - p.price * convert(float, coalesce(d.discount, 0)) / 100.0 as final_price,
       p.category
  from products p
       left outer join discounts d on (d.category = p.category)
 order by p.product_id
;


# MySQL
# Write your MySQL query statement below
select p.product_id, p.price * (1 - coalesce(d.discount, 0)/100) as final_price, p.category
  from products p
       left outer join discounts d on (d.category = p.category)
 order by p.product_id
;


# Pandas
import pandas as pd

def calculate_final_prices(products: pd.DataFrame, discounts: pd.DataFrame) -> pd.DataFrame:
    df = products.merge(discounts, how='left', on='category').fillna(0)
    df['final_price'] = df['price'] - df['price'] * df['discount'] / 100.0
    return df[['product_id', 'final_price', 'category']].sort_values('product_id')

