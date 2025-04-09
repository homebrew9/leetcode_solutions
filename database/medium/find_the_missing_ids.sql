-- Oracle
/* Write your PL/SQL query statement below */
select level as "ids"
from dual
connect by level <= (select max(customer_id) from customers)
minus
select customer_id as "ids" from customers
order by 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select generate_series(1, (select max(customer_id) from customers)) as ids
except
select customer_id from customers
order by 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (max_customer_id) as (
select max(customer_id)
from customers
),
t1 (ids) as (
select 1 as ids
union all
select t1.ids + 1
from t1 cross join t
where t1.ids + 1 <= t.max_customer_id
)
select ids
from t1
where ids not in (select customer_id from customers)
order by 1
;


# MySQL
# Write your MySQL query statement below
with recursive t1 (ids) as (
    select 1 as ids
    union all
    select t1.ids + 1
      from t1
     where t1.ids + 1 <= (select max(customer_id) from customers)
)
select ids
  from t1
 where ids not in (select customer_id
                     from customers
                  )
order by 1
;


# Pandas
import pandas as pd

def find_missing_ids(customers: pd.DataFrame) -> pd.DataFrame:
    max_customer_id = customers['customer_id'].max()
    df = pd.DataFrame(data={'customer_id': pd.Series(range(1, max_customer_id+1))})
    return ( df
            .merge(customers, how='left', on='customer_id')
            .query('customer_name.isnull()')[['customer_id']]
            .rename(columns={'customer_id':'ids'})
            .sort_values('ids')
           )

