-- Oracle
/* Write your PL/SQL query statement below */
with t (invoice_id, product_id, quantity, price, total_price) as (
select pur.invoice_id, pur.product_id, pur.quantity, pur.quantity * prd.price as price,
       sum(pur.quantity * prd.price) over (partition by pur.invoice_id) as total_price
from products prd
     left outer join purchases pur on (pur.product_id = prd.product_id)
)
,
t1 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price,
       max(total_price) over () as max_total_price
from t
)
,
t2 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price
from t1
where total_price = max_total_price
)
,
t3 (invoice_id, product_id, quantity, price, total_price, max_total_price, drnk) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price,
       dense_rank() over (partition by max_total_price order by invoice_id) as drnk
from t2
)
select product_id, quantity, price
from t3
where drnk = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (invoice_id, product_id, quantity, price, total_price) as (
select pur.invoice_id, pur.product_id, pur.quantity, pur.quantity * prd.price as price,
       sum(pur.quantity * prd.price) over (partition by pur.invoice_id) as total_price
from products prd
     left outer join purchases pur on (pur.product_id = prd.product_id)
)
,
t1 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price,
       max(total_price) over () as max_total_price
from t
)
,
t2 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price
from t1
where total_price = max_total_price
)
,
t3 (invoice_id, product_id, quantity, price, total_price, max_total_price, drnk) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price,
       dense_rank() over (partition by max_total_price order by invoice_id) as drnk
from t2
)
select product_id, quantity, price
from t3
where drnk = 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (invoice_id, product_id, quantity, price, total_price) as (
select pur.invoice_id, pur.product_id, pur.quantity, pur.quantity * prd.price as price,
       sum(pur.quantity * prd.price) over (partition by pur.invoice_id) as total_price
from products prd
     left outer join purchases pur on (pur.product_id = prd.product_id)
)
,
t1 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price,
       max(total_price) over () as max_total_price
from t
)
,
t2 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price
from t1
where total_price = max_total_price
)
,
t3 (invoice_id, product_id, quantity, price, total_price, max_total_price, drnk) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price,
       dense_rank() over (partition by max_total_price order by invoice_id) as drnk
from t2
)
select product_id, quantity, price
from t3
where drnk = 1
;


# MySQL
# Write your MySQL query statement below
with t (invoice_id, product_id, quantity, price, total_price) as (
select pur.invoice_id, pur.product_id, pur.quantity, pur.quantity * prd.price as price,
       sum(pur.quantity * prd.price) over (partition by pur.invoice_id) as total_price
from products prd
     left outer join purchases pur on (pur.product_id = prd.product_id)
)
,
t1 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price,
       max(total_price) over () as max_total_price
from t
)
,
t2 (invoice_id, product_id, quantity, price, total_price, max_total_price) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price
from t1
where total_price = max_total_price
)
,
t3 (invoice_id, product_id, quantity, price, total_price, max_total_price, drnk) as (
select invoice_id, product_id, quantity, price, total_price, max_total_price,
       dense_rank() over (partition by max_total_price order by invoice_id) as drnk
from t2
)
select product_id, quantity, price
from t3
where drnk = 1
;


# Pandas
import pandas as pd

def generate_the_invoice(products: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    df = purchases.merge(products, how='inner', on='product_id')
    df['total_price'] = df['quantity'] * df['price']
    df.sort_values(by=['invoice_id','product_id'], inplace=True)
    df['sum_total_price'] = df.groupby('invoice_id')['total_price'].transform('sum')
    df['drnk'] = ( df[df['sum_total_price']==df['sum_total_price'].max()]
                  .groupby('sum_total_price')['invoice_id']
                  .rank(method='dense')
                 )
    return ( df[df['drnk']==1][['product_id','quantity','total_price']]
            .rename(columns={'total_price':'price'})
           )

