-- Oracle
/* Write your PL/SQL query statement below */
with params (start_date, end_date) as (
    select TO_DATE('2023-11-01', 'YYYY-MM-DD'),
           TO_DATE('2023-11-30', 'YYYY-MM-DD')
      from dual
),
t (purchase_date, dow, week_num) as (
    select start_date + level - 1 as purchase_date,
           to_char(start_date + level - 1, 'fmDay') as dow,
           to_char(start_date + level - 1, 'IW') as week_num
      from params
    connect by level <= (end_date - start_date + 1)
),
t1 (week_of_month, purchase_date) as (
    select row_number() over (order by week_num) as week_of_month,
           purchase_date
      from t
     where t.dow = 'Friday'
)
select t1.week_of_month,
       to_char(t1.purchase_date, 'YYYY-MM-DD') as purchase_date,
       sum(p.amount_spend) as total_amount
from t1
     inner join purchases p on (p.purchase_date = t1.purchase_date)
group by t1.week_of_month, t1.purchase_date
order by t1.week_of_month, t1.purchase_date
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
with params (start_date, end_date) as (
    select convert(date, '2023-11-01'), convert(date, '2023-11-30')
),
t (purchase_date, dow, week_num) as (
    select start_date as purchase_date,
           DATENAME(dw, start_date),
           DATEPART(wk, start_date)
      from params
    union all
    select dateadd(day, 1, t.purchase_date),
           DATENAME(dw, dateadd(day, 1, t.purchase_date)),
           DATEPART(wk, dateadd(day, 1, t.purchase_date))
      from t
           cross join params p
     where dateadd(day, 1, t.purchase_date) <= p.end_date
),
t1 (week_of_month, purchase_date) as (
    select row_number() over (order by week_num) as week_of_month,
           purchase_date
      from t
     where t.dow = 'Friday'
)
select t1.week_of_month,
       t1.purchase_date,
       sum(p.amount_spend) as total_amount
from t1
     inner join purchases p on (p.purchase_date = t1.purchase_date)
group by t1.week_of_month, t1.purchase_date
order by t1.week_of_month, t1.purchase_date
;


# MySQL
# Write your MySQL query statement below
with recursive t (purchase_date, dow, week_num) as (
    # WEEKDAY() = 0 for Monday, 4 for Friday
    select '2023-11-01' as purchase_date,
           WEEKDAY('2023-11-01'),
           WEEK('2023-11-01')
    union all
    select date_add(t.purchase_date, interval 1 day),
           WEEKDAY(date_add(t.purchase_date, interval 1 day)),
           WEEK(date_add(t.purchase_date, interval 1 day))
      from t
     where date_add(t.purchase_date, interval 1 day) <= '2023-11-30'
),
t1 (week_of_month, purchase_date) as (
    select row_number() over (order by week_num) as week_of_month,
           purchase_date
      from t
     where t.dow = 4
)
select t1.week_of_month,
       t1.purchase_date,
       sum(p.amount_spend) as total_amount
from t1
     inner join purchases p on (p.purchase_date = t1.purchase_date)
group by t1.week_of_month, t1.purchase_date
order by t1.week_of_month, t1.purchase_date
;


# Pandas
import pandas as pd

def friday_purchases(purchases: pd.DataFrame) -> pd.DataFrame:
    purchases['day_of_week'] = purchases['purchase_date'].dt.strftime('%A')
    purchases['week_of_month'] = (purchases['purchase_date'].dt.strftime('%d').astype(int)/7).apply(math.ceil)
    return ( purchases[purchases['day_of_week'] == 'Friday']
            .groupby(['week_of_month', 'purchase_date'], as_index=0)['amount_spend']
            .sum()
            .rename(columns={'amount_spend': 'total_amount'})
            .sort_values('week_of_month')
           )

