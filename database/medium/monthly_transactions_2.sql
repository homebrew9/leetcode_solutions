-- Oracle
/* Write your PL/SQL query statement below */
with t_approved(month, country, approved_count, approved_amount) as (
    select to_char(trans_date, 'YYYY-MM') as month, country,
           sum(case state when 'approved' then 1 else 0 end) as approved_count,
           sum(case state when 'approved' then amount else 0 end) as approved_amount
      from transactions
     group by to_char(trans_date, 'YYYY-MM'), country
),
t_chargeback (month, country, chargeback_count, chargeback_amount) as (
    select to_char(c.trans_date, 'YYYY-MM') as month, t.country,
           count(*) as chargeback_count,
           sum(t.amount) as chargeback_amount
      from chargebacks c
           inner join transactions t on (t.id = c.trans_id)
     group by to_char(c.trans_date, 'YYYY-MM'), t.country
)
select coalesce(a.month, c.month) as month,
       coalesce(a.country, c.country) as country,
       coalesce(a.approved_count, 0) as approved_count,
       coalesce(a.approved_amount, 0) as approved_amount,
       coalesce(c.chargeback_count, 0) as chargeback_count,
       coalesce(c.chargeback_amount, 0) as chargeback_amount
from t_approved a
     full outer join t_chargeback c on (a.country = c.country and a.month = c.month)
where not (
       coalesce(a.approved_count, 0) = 0 and
       coalesce(a.approved_amount, 0) = 0 and
       coalesce(c.chargeback_count, 0) = 0 and
       coalesce(c.chargeback_amount, 0) = 0
)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t_approved(month, country, approved_count, approved_amount) as (
    select to_char(trans_date, 'YYYY-MM') as month, country,
           sum(case state when 'approved' then 1 else 0 end) as approved_count,
           sum(case state when 'approved' then amount else 0 end) as approved_amount
      from transactions
     group by to_char(trans_date, 'YYYY-MM'), country
),
t_chargeback (month, country, chargeback_count, chargeback_amount) as (
    select to_char(c.trans_date, 'YYYY-MM') as month, t.country,
           count(*) as chargeback_count,
           sum(t.amount) as chargeback_amount
      from chargebacks c
           inner join transactions t on (t.id = c.trans_id)
     group by to_char(c.trans_date, 'YYYY-MM'), t.country
)
select coalesce(a.month, c.month) as month,
       coalesce(a.country, c.country) as country,
       coalesce(a.approved_count, 0) as approved_count,
       coalesce(a.approved_amount, 0) as approved_amount,
       coalesce(c.chargeback_count, 0) as chargeback_count,
       coalesce(c.chargeback_amount, 0) as chargeback_amount
from t_approved a
     full outer join t_chargeback c on (a.country = c.country and a.month = c.month)
where not (
       coalesce(a.approved_count, 0) = 0 and
       coalesce(a.approved_amount, 0) = 0 and
       coalesce(c.chargeback_count, 0) = 0 and
       coalesce(c.chargeback_amount, 0) = 0
)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_approved(month, country, approved_count, approved_amount) as (
    select left(convert(varchar, trans_date, 23), 7) as month, country,
           sum(case state when 'approved' then 1 else 0 end) as approved_count,
           sum(case state when 'approved' then amount else 0 end) as approved_amount
      from transactions
     group by left(convert(varchar, trans_date, 23), 7), country
),
t_chargeback (month, country, chargeback_count, chargeback_amount) as (
    select left(convert(varchar, c.trans_date, 23), 7) as month, t.country,
           count(*) as chargeback_count,
           sum(t.amount) as chargeback_amount
      from chargebacks c
           inner join transactions t on (t.id = c.trans_id)
     group by left(convert(varchar, c.trans_date, 23), 7), t.country
)
select coalesce(a.month, c.month) as month,
       coalesce(a.country, c.country) as country,
       coalesce(a.approved_count, 0) as approved_count,
       coalesce(a.approved_amount, 0) as approved_amount,
       coalesce(c.chargeback_count, 0) as chargeback_count,
       coalesce(c.chargeback_amount, 0) as chargeback_amount
from t_approved a
     full outer join t_chargeback c on (a.country = c.country and a.month = c.month)
where not (
       coalesce(a.approved_count, 0) = 0 and
       coalesce(a.approved_amount, 0) = 0 and
       coalesce(c.chargeback_count, 0) = 0 and
       coalesce(c.chargeback_amount, 0) = 0
)
;


# MySQL
# Write your MySQL query statement below
# MySQL 8.0 does not support FULL OUTER JOINS!!!
with t_approved(month, country, approved_count, approved_amount) as (
    select date_format(trans_date, '%Y-%m') as month, country,
           sum(case state when 'approved' then 1 else 0 end) as approved_count,
           sum(case state when 'approved' then amount else 0 end) as approved_amount
      from transactions
     group by date_format(trans_date, '%Y-%m'), country
),
t_chargeback (month, country, chargeback_count, chargeback_amount) as (
    select date_format(c.trans_date, '%Y-%m') as month, t.country,
           count(*) as chargeback_count,
           sum(t.amount) as chargeback_amount
      from chargebacks c
           inner join transactions t on (t.id = c.trans_id)
     group by date_format(c.trans_date, '%Y-%m'), t.country
),
t_consolidated (month, country, approved_count, approved_amount, chargeback_count, chargeback_amount) as (
select a.month, a.country, a.approved_count, a.approved_amount,
       coalesce(c.chargeback_count, 0) as chargeback_count,
       coalesce(c.chargeback_amount, 0) as chargeback_amount
from t_approved a
     left outer join t_chargeback c on (c.country = a.country and c.month = a.month)
union
select c.month, c.country,
       coalesce(a.approved_count, 0) as approved_count,
       coalesce(a.approved_amount, 0) as approved_amount,
       c.chargeback_count, c.chargeback_amount
from t_approved a
     right outer join t_chargeback c on (c.country = a.country and c.month = a.month)
)
select month, country, approved_count, approved_amount, chargeback_count, chargeback_amount
from t_consolidated
where not (approved_count=0 and approved_amount=0 and chargeback_count=0 and chargeback_amount=0)
;


# Pandas
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame, chargebacks: pd.DataFrame) -> pd.DataFrame:
    transactions['trans_date'] = transactions['trans_date'].dt.strftime('%Y-%m')
    chargebacks['trans_date'] = chargebacks['trans_date'].dt.strftime('%Y-%m')
    df1 = ( transactions[transactions['state']=='approved']
           .groupby(['trans_date','country'],as_index=False)
           .agg(approved_count=('id','count'), approved_amount=('amount','sum'))
           .rename(columns={'trans_date':'month'})
          )
    df2 = ( chargebacks
           .merge(transactions, how='inner', left_on='trans_id', right_on='id')
           .rename(columns={'trans_date_x':'month'})
           .groupby(['month','country'],as_index=False)
           .agg(chargeback_count=('trans_id','count'), chargeback_amount=('amount','sum'))
          )
    return ( df1
            .merge(df2, how='outer', on=['month','country'])
            .fillna(0)
            .query('approved_count != 0 or approved_amount != 0 or chargeback_count != 0 or chargeback_amount != 0')
           )

