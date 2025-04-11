-- Oracle
/* Write your PL/SQL query statement below */
select account_id,
       to_char(day, 'yyyy-mm-dd') as day,
       sum(case type when 'Withdraw' then -amount else amount end) over (partition by account_id order by day) as balance
from transactions
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select account_id, day,
       sum(case type when 'Withdraw' then -amount else amount end) over (partition by account_id order by day) as balance
from transactions
;


-- SQL Server
/* Write your T-SQL query statement below */
select account_id, day,
       sum(case type when 'Withdraw' then -amount else amount end) over (partition by account_id order by day) as balance
from transactions
;


# MySQL
# Write your MySQL query statement below
select account_id, day,
       sum(case type when 'Withdraw' then -amount else amount end) over (partition by account_id order by day) as balance
from transactions
;


# Pandas
import pandas as pd

def account_balance(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['upd_amount'] = (np.where(transactions['type']=='Withdraw',-transactions['amount'],transactions['amount']
                                          ).astype(int)
                                 )
    transactions.sort_values(['account_id','day'], inplace=True)
    transactions['balance'] = transactions.groupby(['account_id'])['upd_amount'].cumsum()
    return transactions[['account_id','day','balance']]

