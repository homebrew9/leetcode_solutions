-- Oracle
/* Write your PL/SQL query statement below */
select u.name, sum(t.amount) as balance
  from users u
       inner join transactions t on (t.account = u.account)
 group by u.name
having sum(t.amount) > 10000
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select account, sum(amount) as balance
    from transactions
    group by account
    having sum(amount) > 10000
)
select u.name, t.balance
from users u
     inner join t on (t.account = u.account)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select account, sum(amount) as balance
    from transactions
    group by account
    having sum(amount) > 10000
)
select u.name, t.balance
from users u
     inner join t on (t.account = u.account)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select account, sum(amount) as balance
    from transactions
    group by account
    having sum(amount) > 10000
)
select u.name, t.balance
from users u
     inner join t on (t.account = u.account)
;


# Pandas
import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    return ( users
            .merge(transactions, how='inner', on='account')
            .groupby(['account','name'],as_index=0)['amount']
            .sum()
            .query('amount > 10000')[['name','amount']]
            .rename(columns={'amount': 'balance'})
           )

