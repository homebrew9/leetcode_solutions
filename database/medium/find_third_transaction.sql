-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, spend, transaction_date, trx_no, prev_trx_1, prev_trx_2) as (
select user_id, spend, transaction_date,
       row_number() over (partition by user_id order by transaction_date) as trx_no,
       lag(spend) over (partition by user_id order by transaction_date) as prev_trx_1,
       lag(spend, 2) over (partition by user_id order by transaction_date) as prev_trx_2
from transactions
)
select user_id,
       spend as third_transaction_spend,
       transaction_date as third_transaction_date
from t
where trx_no = 3
and spend > prev_trx_1
and spend > prev_trx_2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, spend, transaction_date, trx_no, prev_trx_1, prev_trx_2) as (
select user_id, spend, transaction_date,
       row_number() over (partition by user_id order by transaction_date) as trx_no,
       lag(spend) over (partition by user_id order by transaction_date) as prev_trx_1,
       lag(spend, 2) over (partition by user_id order by transaction_date) as prev_trx_2
from transactions
)
select user_id,
       spend as third_transaction_spend,
       transaction_date as third_transaction_date
from t
where trx_no = 3
and spend > prev_trx_1
and spend > prev_trx_2
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, spend, transaction_date, trx_no, prev_trx_1, prev_trx_2) as (
select user_id, spend, transaction_date,
       row_number() over (partition by user_id order by transaction_date) as trx_no,
       lag(spend) over (partition by user_id order by transaction_date) as prev_trx_1,
       lag(spend, 2) over (partition by user_id order by transaction_date) as prev_trx_2
from transactions
)
select user_id,
       spend as third_transaction_spend,
       transaction_date as third_transaction_date
from t
where trx_no = 3
and spend > prev_trx_1
and spend > prev_trx_2
;


# MySQL
# Write your MySQL query statement below
with t (user_id, spend, transaction_date, trx_no, prev_trx_1, prev_trx_2) as (
select user_id, spend, transaction_date,
       row_number() over (partition by user_id order by transaction_date) as trx_no,
       lag(spend) over (partition by user_id order by transaction_date) as prev_trx_1,
       lag(spend, 2) over (partition by user_id order by transaction_date) as prev_trx_2
from transactions
)
select user_id,
       spend as third_transaction_spend,
       transaction_date as third_transaction_date
from t
where trx_no = 3
and spend > prev_trx_1
and spend > prev_trx_2
;


# Pandas
import pandas as pd

def find_third_transaction(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['drnk'] = transactions.groupby('user_id')['transaction_date'].rank(method='dense')
    transactions = transactions.sort_values(by=['user_id','drnk'])
    transactions['prev_day1_spend'] = transactions.shift(1)['spend']
    transactions['prev_day2_spend'] = transactions.shift(2)['spend']
    return ( transactions
            .query('drnk==3 and spend > prev_day1_spend and spend > prev_day2_spend')
             [['user_id','spend','transaction_date']]
            .sort_values('user_id')
            .rename(columns={'spend': 'third_transaction_spend', 'transaction_date': 'third_transaction_date'})
           )

