-- Oracle
/* Write your PL/SQL query statement below */
select to_char(transaction_date, 'yyyy-mm-dd') as transaction_date,
       sum(case when mod(amount, 2) = 1 then amount else 0 end) as odd_sum,
       sum(case when mod(amount, 2) = 0 then amount else 0 end) as even_sum
  from transactions
 group by transaction_date
 order by transaction_date
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select to_char(transaction_date, 'yyyy-mm-dd') as transaction_date,
       sum(case when mod(amount, 2) = 1 then amount else 0 end) as odd_sum,
       sum(case when mod(amount, 2) = 0 then amount else 0 end) as even_sum
  from transactions
 group by transaction_date
 order by transaction_date
;


-- SQL Server
/* Write your T-SQL query statement below */
select transaction_date,
       sum(case when amount % 2 = 1 then amount else 0 end) as odd_sum,
       sum(case when amount % 2 = 0 then amount else 0 end) as even_sum
  from transactions
 group by transaction_date
 order by transaction_date
;


# MySQL
# Write your MySQL query statement below
select transaction_date,
       sum(case when mod(amount, 2) = 1 then amount else 0 end) as odd_sum,
       sum(case when mod(amount, 2) = 0 then amount else 0 end) as even_sum
  from transactions
 group by transaction_date
 order by transaction_date
;


# Pandas
import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['parity'] = np.where(transactions['amount'] % 2 == 1, 'odd_sum', 'even_sum')
    df = transactions.groupby(['transaction_date', 'parity'], as_index=0)['amount'].sum()
    return ( df
            .pivot(columns='parity', values='amount', index='transaction_date')
            .reset_index()
            .fillna(0)[['transaction_date', 'odd_sum', 'even_sum']]
            .sort_values('transaction_date')
           )

