-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select product_id,
       trunc(purchase_date, 'yyyy') as purchase_year,
       count(*) as cnt
from orders
group by product_id, trunc(purchase_date, 'yyyy')
)
select distinct t.product_id --, t.purchase_year, t.cnt, t1.cnt
from t
     inner join t t1
     on (t1.product_id = t.product_id and t1.purchase_year = trunc(add_months(t.purchase_year,12),'yyyy'))
where t.cnt >= 3
and t1.cnt >= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select product_id,
       date_trunc('year', purchase_date) as purchase_year,
       count(*) as cnt
from orders
group by product_id, date_trunc('year', purchase_date)
)
select distinct t.product_id
from t
     inner join t t1
     on (
            t1.product_id = t.product_id
            and
            t1.purchase_year =  t.purchase_year + interval '1 year'
        )
where t.cnt >= 3
and t1.cnt >= 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select product_id,
       CONVERT(DATETIME, CONVERT(VARCHAR(4), purchase_date, 120) + '-01-01') as purchase_year,
       count(*) as cnt
from orders
group by product_id,
         CONVERT(DATETIME, CONVERT(VARCHAR(4), purchase_date, 120) + '-01-01')
)
select distinct t.product_id
from t
     inner join t t1
     on (
            t1.product_id = t.product_id
            and
            t1.purchase_year = DATEADD(YEAR, 1, t.purchase_year)
        )
where t.cnt >= 3
and t1.cnt >= 3
;


# MySQL
# Write your MySQL query statement below
with t as (
select product_id,
       str_to_date(DATE_FORMAT(purchase_date, '%Y-01-01'), '%Y-%m-%d') as purchase_year,
       count(*) as cnt
from orders
group by product_id,
         str_to_date(DATE_FORMAT(purchase_date, '%Y-01-01'), '%Y-%m-%d')
)
select distinct t.product_id
from t
     inner join t t1
     on (
            t1.product_id = t.product_id
            and
            t1.purchase_year =  t.purchase_year + interval 1 year
        )
where t.cnt >= 3
and t1.cnt >= 3
;


# Pandas
import pandas as pd

def find_valid_products(orders: pd.DataFrame) -> pd.DataFrame:
    orders['purchase_year'] = orders['purchase_date'].dt.strftime('%Y').astype('int')
    df = ( orders
          .groupby(['product_id','purchase_year'], as_index=0)['order_id']
          .count()
          .rename(columns={'order_id': 'order_count'})
         )
    return ( df
            .merge(df, how='inner', on='product_id')
            .query('order_count_x >= 3 and order_count_y >= 3 and purchase_year_y == purchase_year_x + 1')[['product_id']]
            .drop_duplicates()
           )

