-- Oracle
/* Write your PL/SQL query statement below */
with t (mth) as (
    select '2020-06' as mth from dual union all
    select '2020-07' from dual
),
t1 (customer_id, name, mth, total_expense) as (
    select c.customer_id, c.name, to_char(order_date, 'YYYY-MM') as mth,
           sum(o.quantity * p.price) as total_expense
      from orders o
           inner join customers c on (c.customer_id = o.customer_id)
           inner join product p on (p.product_id = o.product_id)
     where to_char(order_date, 'YYYY-MM') in ('2020-06', '2020-07')
     group by c.customer_id, c.name, to_char(order_date, 'YYYY-MM')
     having sum(o.quantity * p.price) >= 100
)
select t1.customer_id, t1.name
  from t
       left outer join t1 on (t1.mth = t.mth)
 group by t1.customer_id, t1.name
having count(*) = 2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (mth) as (
    select '2020-06' as mth union all
    select '2020-07'
),
t1 (customer_id, name, mth, total_expense) as (
    select c.customer_id, c.name, to_char(order_date, 'YYYY-MM') as mth,
           sum(o.quantity * p.price) as total_expense
      from orders o
           inner join customers c on (c.customer_id = o.customer_id)
           inner join product p on (p.product_id = o.product_id)
     where to_char(order_date, 'YYYY-MM') in ('2020-06', '2020-07')
     group by c.customer_id, c.name, to_char(order_date, 'YYYY-MM')
     having sum(o.quantity * p.price) >= 100
)
select t1.customer_id, t1.name
  from t
       left outer join t1 on (t1.mth = t.mth)
 group by t1.customer_id, t1.name
having count(*) = 2
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (customer_id, name, mth, total_sales) as (
select c.customer_id, c.name,
       CONVERT(DATETIME, CONVERT(VARCHAR(7), o.order_date, 120) + '-01') as mth,
       sum(o.quantity*p.price) as total_sales
from orders o
     inner join product p on (p.product_id = o.product_id)
     inner join customers c on (c.customer_id = o.customer_id)
where CONVERT(DATETIME, CONVERT(VARCHAR(7), o.order_date, 120) + '-01') in ('2020-06-01', '2020-07-01')
group by c.customer_id, c.name,
         CONVERT(DATETIME, CONVERT(VARCHAR(7), o.order_date, 120) + '-01')
having sum(o.quantity*p.price) >= 100
)
select c.customer_id, c.name
from customers c
where exists (select null from t where t.customer_id = c.customer_id and t.mth = '2020-06-01')
and exists (select null from t where t.customer_id = c.customer_id and t.mth = '2020-07-01')
;


# MySQL
# Write your MySQL query statement below
with t (customer_id, name, mth, total_sales) as (
select c.customer_id, c.name,
       DATE_FORMAT(o.order_date, '%Y-%m-01') as mth,
       sum(o.quantity*p.price) as total_sales
from orders o
     inner join product p on (p.product_id = o.product_id)
     inner join customers c on (c.customer_id = o.customer_id)
where DATE_FORMAT(o.order_date, '%Y-%m-01') in ('2020-06-01', '2020-07-01')
group by c.customer_id, c.name,
         DATE_FORMAT(o.order_date, '%Y-%m-01')
having sum(o.quantity*p.price) >= 100
)
select c.customer_id, c.name
from customers c
where exists (select null from t where t.customer_id = c.customer_id and t.mth = '2020-06-01')
and exists (select null from t where t.customer_id = c.customer_id and t.mth = '2020-07-01')
;


# Pandas
import pandas as pd

def customer_order_frequency(customers: pd.DataFrame, product: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Fetch orders in June and July 2020
    jun_jul_orders = orders[(orders['order_date']>='2020-06-01') & (orders['order_date']<='2020-07-31')]
    
    # Merge with Product dataframe to access the prices
    orders_and_sales = jun_jul_orders.merge(product, how='inner', on='product_id')
    
    # Add month and sales derived columns to facilitate groupby
    orders_and_sales['mth'] = orders_and_sales['order_date'].dt.strftime('%Y-%m')
    orders_and_sales['sales'] = orders_and_sales['quantity']*orders_and_sales['price']
    
    # Group by month and filter on sales >= 100
    total_sales = orders_and_sales.groupby(by=['customer_id','mth'],as_index=False)['sales'].sum().query('sales >= 100')
    
    # Our target customers should have two records now, one for June and one for July
    target_customers = total_sales.groupby('customer_id',as_index=False)['mth'].count().query('mth == 2')['customer_id']
    
    # Return the id and names of target customers
    return customers[customers['customer_id'].isin(target_customers)][['customer_id','name']]

