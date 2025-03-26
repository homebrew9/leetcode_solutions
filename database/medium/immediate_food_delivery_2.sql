-- Oracle
/* Write your PL/SQL query statement below */
select round(count(*) / y.total_customers * 100, 2) as immediate_percentage
from (
select delivery_id, customer_id, order_date, customer_pref_delivery_date,
       min(order_date) over (partition by customer_id) as first_order_date
from delivery
) x  cross join (select count(distinct customer_id) as total_customers from delivery) y
where x.customer_pref_delivery_date = x.first_order_date
group by y.total_customers
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (total_customers) as (
    select count(distinct customer_id)::numeric from delivery
),
t1 (customer_id, order_date, customer_pref_delivery_date, rnk) as (
    select customer_id, order_date, customer_pref_delivery_date,
           rank() over (partition by customer_id order by order_date) as rnk
    from delivery d
)
select round(
              sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)
              /
              t.total_customers * 100,
              2
            ) as immediate_percentage
  from t1
       cross join t
 where rnk = 1
 group by t.total_customers
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (total_customers) as (
    select convert(float, count(distinct customer_id)) from delivery
),
t1 (customer_id, order_date, customer_pref_delivery_date, rnk) as (
    select customer_id, order_date, customer_pref_delivery_date,
           rank() over (partition by customer_id order by order_date) as rnk
    from delivery d
)
select round(
              sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)
              /
              t.total_customers * 100,
              2
            ) as immediate_percentage
  from t1
       cross join t
 where rnk = 1
 group by t.total_customers
;


# MySQL
# Write your MySQL query statement below
with t (total_customers) as (
    select count(distinct customer_id) from delivery
),
t1 (customer_id, order_date, customer_pref_delivery_date, rnk) as (
    select customer_id, order_date, customer_pref_delivery_date,
           rank() over (partition by customer_id order by order_date) as rnk
    from delivery d
)
select round(
              sum(case when order_date = customer_pref_delivery_date then 1 else 0 end)
              /
              t.total_customers * 100,
              2
            ) as immediate_percentage
  from t1
       cross join t
 where rnk = 1
 group by t.total_customers
;


# Pandas
import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    total_customers = delivery['customer_id'].drop_duplicates().count()
    delivery['rnk'] = delivery.groupby('customer_id', as_index=False)['order_date'].rank(method='first')
    immediate_orders = ( delivery[(delivery['rnk']==1)
                                   &
                                  (delivery['order_date']==delivery['customer_pref_delivery_date'])
                                 ]['customer_id']
                         .count()
                       )
    return pd.DataFrame(data={'immediate_percentage': [round(immediate_orders/total_customers * 100, 2)]})

