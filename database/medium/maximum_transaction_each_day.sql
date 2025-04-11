-- Oracle
/* Write your PL/SQL query statement below */
with t (day, transaction_id, amount, drnk) as (
    select day, transaction_id, amount,
           dense_rank() over (partition by trunc(day) order by amount desc) as drnk
      from transactions
)
select transaction_id
  from t
 where drnk = 1
 order by transaction_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (transaction_id, day, amount, drnk) as (
select transaction_id, day, amount,
       dense_rank() over (partition by day order by amount desc) as drnk
from transactions
)
select transaction_id
from t
where drnk = 1
order by transaction_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (transaction_id, day, amount, drnk) as (
select transaction_id, day, amount,
       dense_rank() over (partition by convert(varchar, day, 23) order by amount desc) as drnk
from transactions
)
select transaction_id
from t
where drnk = 1
order by transaction_id
;


# MySQL
# Write your MySQL query statement below
with t (transaction_id, day, amount, drnk) as (
select transaction_id, day, amount,
       dense_rank() over (partition by day order by amount desc) as drnk
from transactions
)
select transaction_id
from t
where drnk = 1
order by transaction_id
;


# Pandas
import pandas as pd

def find_maximum_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['day_fmt'] = transactions['day'].dt.strftime('%Y-%m-%d')
    return (  transactions.assign(drnk=transactions.groupby('day_fmt')['amount']
                                                   .rank('dense',ascending=0)
                                 )
                          .query('drnk==1')[['transaction_id']]
                          .sort_values('transaction_id')
           )

