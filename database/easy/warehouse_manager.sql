-- Oracle
/* Write your PL/SQL query statement below */
select w.name as warehouse_name,
       sum(w.units * p.width * p.length * p.height) as volume
  from warehouse w
       inner join products p on (p.product_id = w.product_id)
 group by w.name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select w.name as warehouse_name,
       sum(w.units * (p.width * p.length * p.height)) as volume
from warehouse w
     inner join products p on (p.product_id = w.product_id)
group by w.name
;


-- SQL Server
/* Write your T-SQL query statement below */
select w.name as warehouse_name,
       sum(w.units * (p.width * p.length * p.height)) as volume
from warehouse w
     inner join products p on (p.product_id = w.product_id)
group by w.name
;


# MySQL
# Write your MySQL query statement below
select w.name as warehouse_name,
       sum(w.units * (p.width * p.length * p.height)) as volume
from warehouse w
     inner join products p on (p.product_id = w.product_id)
group by w.name
;


# Pandas
import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    df = warehouse.merge(products, how='inner', on='product_id')
    df['vol'] = df['units'] * df['Width'] * df['Length'] * df['Height']
    return df.groupby('name', as_index=False)['vol'].sum().rename(columns={'name':'warehouse_name', 'vol':'volume'})

