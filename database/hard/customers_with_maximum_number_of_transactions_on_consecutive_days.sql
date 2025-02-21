-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select customer_id,
           transaction_date - row_number() over (partition by customer_id order by transaction_date) as group_id
      from transactions
),
t1 as (
    select customer_id, group_id, count(*) as consecutive_days
      from t
     group by customer_id, group_id
)
select customer_id
  from t1
 where consecutive_days = (select max(consecutive_days) from t1)
 order by customer_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (customer_id, transaction_date, root, depth) as (
    select customer_id, transaction_date, transaction_date, 1 as depth
      from transactions
    union all
    select t1.customer_id, t1.transaction_date, t.root, t.depth + 1
      from transactions t1
           inner join t on (t.customer_id = t1.customer_id and
                            t1.transaction_date = t.transaction_date + interval '1 day'
                           )
),
t1 as (
    select customer_id, root, count(*) as consecutive_days
      from t
     group by customer_id, root
)
select customer_id
  from t1
 where consecutive_days = (select max(consecutive_days) from t1)
 order by customer_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (customer_id, transaction_date, root, depth) as (
    select customer_id, transaction_date, transaction_date, 1 as depth
      from transactions
    union all
    select t1.customer_id, t1.transaction_date, t.root, t.depth + 1
      from transactions t1
           inner join t on (t.customer_id = t1.customer_id and
                            t1.transaction_date = DATEADD(DAY, 1, t.transaction_date)
                           )
),
t1 as (
    select customer_id, root, count(*) as consecutive_days
      from t
     group by customer_id, root
)
select customer_id
  from t1
 where consecutive_days = (select max(consecutive_days) from t1)
 order by customer_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select customer_id,
           transaction_date - row_number() over (partition by customer_id order by transaction_date) as group_id
      from transactions
),
t1 as (
    select customer_id, group_id, count(*) as consecutive_days
      from t
     group by customer_id, group_id
)
select customer_id
  from t1
 where consecutive_days = (select max(consecutive_days) from t1)
 order by customer_id
;


# Pandas
import pandas as pd

def find_customers(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions.sort_values(['customer_id','transaction_date'], inplace=True)
    transactions['rn'] = transactions.groupby('customer_id').cumcount()+1
    transactions['group_id'] = transactions['transaction_date'] - pd.to_timedelta(transactions['rn'], unit='d')
    df = transactions.groupby(['customer_id','group_id'], as_index=0)['rn'].count()
    return df[df['rn'] == df['rn'].max()][['customer_id']].sort_values('customer_id')

