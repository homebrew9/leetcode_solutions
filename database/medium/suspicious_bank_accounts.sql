-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select account_id, trunc(day, 'MM') as mth, sum(amount) as total_income
from transactions
where type = 'Creditor'
group by account_id, trunc(day, 'MM')
),
t1 as (
select a.account_id, a.max_income, t.mth, t.total_income,
       lag(t.mth) over (partition by a.account_id order by t.mth) as prev_mth,
       lag(total_income) over (partition by a.account_id order by t.mth) as prev_mth_income
from accounts a
     inner join t on (t.account_id = a.account_id)
)
--select * from t1;
select distinct account_id
from t1
where total_income > max_income
and prev_mth = add_months(mth, -1)
and prev_mth_income > max_income
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select account_id, date_trunc('month', day) as mth, sum(amount) as total_income
from transactions
where type = 'Creditor'
group by account_id, date_trunc('month', day)
),
t1 as (
select a.account_id, a.max_income, t.mth, t.total_income,
       lag(t.mth) over (partition by a.account_id order by t.mth) as prev_mth,
       lag(total_income) over (partition by a.account_id order by t.mth) as prev_mth_income
from accounts a
     inner join t on (t.account_id = a.account_id)
)
--select * from t1;
select distinct account_id
from t1
where total_income > max_income
and prev_mth = mth - interval '1 month'
and prev_mth_income > max_income
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select account_id,
       CONVERT(DATETIME, CONVERT(VARCHAR(7), day, 120) + '-01') as mth,
       sum(amount) as total_income
from transactions
where type = 'Creditor'
group by account_id,
         CONVERT(DATETIME, CONVERT(VARCHAR(7), day, 120) + '-01')
),
t1 as (
select a.account_id, a.max_income, t.mth, t.total_income,
       lag(t.mth) over (partition by a.account_id order by t.mth) as prev_mth,
       lag(total_income) over (partition by a.account_id order by t.mth) as prev_mth_income
from accounts a
     inner join t on (t.account_id = a.account_id)
)
--select * from t1;
select distinct account_id
from t1
where total_income > max_income
and prev_mth = DATEADD(MONTH, -1, mth)
and prev_mth_income > max_income
;


# MySQL
# Write your MySQL query statement below
with t as (
select account_id,
       str_to_date(DATE_FORMAT(day, '%Y-%m-01'), '%Y-%m-%d') as mth,
       sum(amount) as total_income
from transactions
where type = 'Creditor'
group by account_id,
         str_to_date(DATE_FORMAT(day, '%Y-%m-01'), '%Y-%m-%d')
),
t1 as (
select a.account_id, a.max_income, t.mth, t.total_income,
       lag(t.mth) over (partition by a.account_id order by t.mth) as prev_mth,
       lag(total_income) over (partition by a.account_id order by t.mth) as prev_mth_income
from accounts a
     inner join t on (t.account_id = a.account_id)
)
#select * from t1;
select distinct account_id
from t1
where total_income > max_income
and prev_mth = mth - interval 1 month
and prev_mth_income > max_income
;


# Pandas
import pandas as pd

def suspicious_bank_accounts(accounts: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['day'].dt.strftime('%Y%m').astype('int')
    df = ( transactions[transactions['type']=='Creditor']
          .groupby(['account_id','month'], as_index=0)['amount']
          .sum()
          .merge(accounts, how='inner', on='account_id')
          .query('amount > max_income')
          .sort_values(['account_id', 'month'])
         )
    df['prev_account_id'] = df['account_id'].shift(1)
    df['prev_month'] = df['month'].shift(1)
    return ( df
            .query('account_id == prev_account_id and month == prev_month + 1')[['account_id']]
            .drop_duplicates()
           )

