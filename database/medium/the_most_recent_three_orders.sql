-- Oracle
/* Write your PL/SQL query statement below */
with t (customer_name, customer_id, order_id, order_date, drnk) as (
    select c.name as customer_name, o.customer_id, o.order_id, o.order_date,
           dense_rank() over (partition by o.customer_id order by o.order_date desc) as drnk
      from orders o
           inner join customers c on (c.customer_id = o.customer_id)
)
select customer_name, customer_id, order_id, to_char(order_date, 'YYYY-MM-DD') as order_date
  from t
 where drnk <= 3
 order by customer_name, customer_id, order_date desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (customer_name, customer_id, order_id, order_date, drnk) as (
select c.name as customer_name, c.customer_id, o.order_id, o.order_date,
       dense_rank() over (partition by c.customer_id order by o.order_date desc) as drnk
from customers c
     inner join orders o on (o.customer_id = c.customer_id)
)
select customer_name, customer_id, order_id, order_date
from t
where drnk <= 3
order by customer_name, customer_id, order_date desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (customer_name, customer_id, order_id, order_date, drnk) as (
select c.name as customer_name, c.customer_id, o.order_id, o.order_date,
       dense_rank() over (partition by c.customer_id order by o.order_date desc) as drnk
from customers c
     inner join orders o on (o.customer_id = c.customer_id)
)
select customer_name, customer_id, order_id, order_date
from t
where drnk <= 3
order by customer_name, customer_id, order_date desc
;


# MySQL
# Write your MySQL query statement below
with t (customer_name, customer_id, order_id, order_date, drnk) as (
select c.name as customer_name, c.customer_id, o.order_id, o.order_date,
       dense_rank() over (partition by c.customer_id order by o.order_date desc) as drnk
from customers c
     inner join orders o on (o.customer_id = c.customer_id)
)
select customer_name, customer_id, order_id, order_date
from t
where drnk <= 3
order by customer_name, customer_id, order_date desc
;


# Pandas
import pandas as pd

def recent_three_orders(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how='inner', on='customer_id')
    return ( df
            .assign(drnk=df.groupby(['customer_id','name'], as_index=False)['order_date']
                           .rank(method='dense', ascending=False)
            )
            .query('drnk <= 3')
            .sort_values(by=['name','customer_id','order_date'], ascending=[True,True,False])[['name','customer_id','order_id','order_date']]
            .rename(columns={'name': 'customer_name'})
           )

