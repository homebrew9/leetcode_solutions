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

