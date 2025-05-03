-- Oracle
/* Write your PL/SQL query statement below */
select u.name, sum(t.amount) as balance
  from users u
       inner join transactions t on (t.account = u.account)
 group by u.name
having sum(t.amount) > 10000
;


-- PostgreSQL


-- SQL Server


# MySQL


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

