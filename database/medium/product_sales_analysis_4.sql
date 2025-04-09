-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, product_id, total_spent) as (
select s.user_id, s.product_id, sum(s.quantity * p.price) as total_spent
from sales s
     inner join product p on (p.product_id = s.product_id)
group by s.user_id, s.product_id
),
t1 (user_id, product_id, total_spent, max_spent) as (
select t.user_id, t.product_id, t.total_spent,
       max(t.total_spent) over (partition by t.user_id) as max_spent
from t
)
select t1.user_id, t1.product_id
from t1
where total_spent = max_spent
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, product_id, total_spent) as (
select s.user_id, s.product_id, sum(s.quantity * p.price) as total_spent
from sales s
     inner join product p on (p.product_id = s.product_id)
group by s.user_id, s.product_id
),
t1 (user_id, product_id, total_spent, max_spent) as (
select t.user_id, t.product_id, t.total_spent,
       max(t.total_spent) over (partition by t.user_id) as max_spent
from t
)
select t1.user_id, t1.product_id
from t1
where total_spent = max_spent
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, product_id, total_spent) as (
select s.user_id, s.product_id, sum(s.quantity * p.price) as total_spent
from sales s
     inner join product p on (p.product_id = s.product_id)
group by s.user_id, s.product_id
),
t1 (user_id, product_id, total_spent, max_spent) as (
select t.user_id, t.product_id, t.total_spent,
       max(t.total_spent) over (partition by t.user_id) as max_spent
from t
)
select t1.user_id, t1.product_id
from t1
where total_spent = max_spent
;


# MySQL
# Write your MySQL query statement below
with t (user_id, product_id, total_spent) as (
select s.user_id, s.product_id, sum(s.quantity * p.price) as total_spent
from sales s
     inner join product p on (p.product_id = s.product_id)
group by s.user_id, s.product_id
),
t1 (user_id, product_id, total_spent, max_spent) as (
select t.user_id, t.product_id, t.total_spent,
       max(t.total_spent) over (partition by t.user_id) as max_spent
from t
)
select t1.user_id, t1.product_id
from t1
where total_spent = max_spent
;


# Pandas
import pandas as pd

def product_sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product, how='inner', on='product_id')
    df['amt_spent'] = df['quantity']*df['price']
    df = df.groupby(['user_id','product_id'],as_index=False)['amt_spent'].sum()
    df = df.assign(max_amt_spent=df.groupby('user_id')['amt_spent'].transform('max'))
    return df[df['amt_spent']==df['max_amt_spent']][['user_id','product_id']]

