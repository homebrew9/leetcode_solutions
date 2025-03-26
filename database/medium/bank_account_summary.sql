-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, total_amount) as (
select x.user_id, sum(x.amount) as total_amount
from (
        select paid_by as user_id, -amount as amount from transactions
        union all
        select paid_to as user_id, amount from transactions
     ) x
group by x.user_id
)
select u.user_id, u.user_name,
       u.credit + coalesce(t.total_amount, 0) as credit,
       case when u.credit + coalesce(t.total_amount, 0) < 0 then 'Yes' else 'No' end as credit_limit_breached
from users u
     left outer join t on (t.user_id = u.user_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, total_amount) as (
select x.user_id, sum(x.amount) as total_amount
from (
        select paid_by as user_id, -amount as amount from transactions
        union all
        select paid_to as user_id, amount from transactions
     ) x
group by x.user_id
)
select u.user_id, u.user_name,
       u.credit + coalesce(t.total_amount, 0) as credit,
       case when u.credit + coalesce(t.total_amount, 0) < 0 then 'Yes' else 'No' end as credit_limit_breached
from users u
     left outer join t on (t.user_id = u.user_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, total_amount) as (
select x.user_id, sum(x.amount) as total_amount
from (
        select paid_by as user_id, -amount as amount from transactions
        union all
        select paid_to as user_id, amount from transactions
     ) x
group by x.user_id
)
select u.user_id, u.user_name,
       u.credit + coalesce(t.total_amount, 0) as credit,
       case when u.credit + coalesce(t.total_amount, 0) < 0 then 'Yes' else 'No' end as credit_limit_breached
from users u
     left outer join t on (t.user_id = u.user_id)
;


# MySQL
# Write your MySQL query statement below
with t (user_id, total_amount) as (
select x.user_id, sum(x.amount) as total_amount
from (
        select paid_by as user_id, -amount as amount from transactions
        union all
        select paid_to as user_id, amount from transactions
     ) x
group by x.user_id
)
select u.user_id, u.user_name,
       u.credit + coalesce(t.total_amount, 0) as credit,
       case when u.credit + coalesce(t.total_amount, 0) < 0 then 'Yes' else 'No' end as credit_limit_breached
from users u
     left outer join t on (t.user_id = u.user_id)
;


# Pandas
import pandas as pd

def bank_account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = ( users
          .merge( transactions
                 .groupby('paid_to',as_index=0)['amount']
                 .sum(), how='left', left_on='user_id',  right_on='paid_to'
                )
          .fillna(0)
    )
    df = ( df
          .merge( transactions
                 .groupby('paid_by',as_index=0)['amount']
                 .sum(), how='left', left_on='user_id', right_on='paid_by'
                )
          .fillna(0)
    )
    df['credit'] = df['credit'] + df['amount_x'] - df['amount_y']
    df['credit_limit_breached'] = np.where(df['credit'] < 0, 'Yes', 'No')
    return df[['user_id','user_name','credit','credit_limit_breached']]

