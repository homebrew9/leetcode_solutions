-- Oracle
/* Write your PL/SQL query statement below */
with cal (num) as (
    select 1 as num
      from dual
    union all
    select c.num + 1
      from cal c
     where c.num <= DATE'2020-01-01' - DATE'2019-01-01' - 1
)
,
calendar (dt) as (
    select DATE'2019-01-01' + num - 1
      from cal
)
,
f1 (fail_date, epoch, group_id) as (
    select f.fail_date, DATE'2019-01-01' + row_number() over (order by f.fail_date) - 1 as epoch,
           f.fail_date - (DATE'2019-01-01' + row_number() over (order by f.fail_date) - 1) as group_id
      from failed f
           inner join calendar c on (f.fail_date = c.dt)
)
,
f2 (period_state, start_date, end_date) as (
    select 'failed' as period_state, min(fail_date) as start_date, max(fail_date) as end_date
      from f1
     group by group_id
)
,
s1 (success_date, epoch, group_id) as (
    select s.success_date, DATE'2019-01-01' + row_number() over (order by s.success_date) - 1 as epoch,
           s.success_date - (DATE'2019-01-01' + row_number() over (order by s.success_date) - 1) as group_id
      from succeeded s
           inner join calendar c on (s.success_date = c.dt)
)
,
s2 (period_state, start_date, end_date) as (
    select 'succeeded' as period_state, min(success_date) as start_date, max(success_date) as end_date
      from s1
     group by group_id
)
select f2.period_state as period_state, to_char(f2.start_date, 'YYYY-MM-DD') as start_date, to_char(f2.end_date, 'YYYY-MM-DD') as end_date
  from f2
union all
select s2.period_state as period_state, to_char(s2.start_date, 'YYYY-MM-DD') as start_date, to_char(s2.end_date, 'YYYY-MM-DD') as end_date
  from s2
order by start_date
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (period_state, status_date) as (
select 'failed', fail_date
from failed
where to_char(fail_date, 'yyyy') = '2019'
union all
select 'succeeded', success_date
from succeeded
where to_char(success_date, 'yyyy') = '2019'
),
t1 (period_state, status_date, status_change) as (
select period_state, status_date,
       case when lag(period_state) over (order by status_date) is null or
                 period_state != lag(period_state) over (order by status_date)
       then 1
       else 0
       end as status_change
from t
),
t2 (period_state, status_date, status_change, group_id) as (
select period_state, status_date, status_change,
       sum(status_change) over (order by status_date rows between unbounded preceding and current row) as group_id
from t1
)
select period_state,
       to_char(min(status_date), 'YYYY-MM-DD') as start_date,
       to_char(max(status_date), 'YYYY-MM-DD') as end_date
from t2
group by group_id, period_state
order by group_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (period_state, status_date) as (
select 'failed', fail_date
from failed
where year(fail_date) = 2019
union all
select 'succeeded', success_date
from succeeded
where year(success_date) = 2019
),
t1 (period_state, status_date, status_change) as (
select period_state, status_date,
       case when lag(period_state) over (order by status_date) is null or
                 period_state != lag(period_state) over (order by status_date)
       then 1
       else 0
       end as status_change
from t
),
t2 (period_state, status_date, status_change, group_id) as (
select period_state, status_date, status_change,
       sum(status_change) over (order by status_date rows between unbounded preceding and current row) as group_id
from t1
)
select period_state,
       min(status_date) as start_date,
       max(status_date) as end_date
from t2
group by group_id, period_state
order by group_id
;


# MySQL
# Write your MySQL query statement below
with t (period_state, status_date) as (
select 'failed', fail_date
from failed
where year(fail_date) = 2019
union all
select 'succeeded', success_date
from succeeded
where year(success_date) = 2019
),
t1 (period_state, status_date, status_change) as (
select period_state, status_date,
       case when lag(period_state) over (order by status_date) is null or
                 period_state != lag(period_state) over (order by status_date)
       then 1
       else 0
       end as status_change
from t
),
t2 (period_state, status_date, status_change, group_id) as (
select period_state, status_date, status_change,
       sum(status_change) over (order by status_date rows between unbounded preceding and current row) as group_id
from t1
)
select period_state,
       min(status_date) as start_date,
       max(status_date) as end_date
from t2
group by group_id, period_state
order by group_id
;


# Pandas
import pandas as pd

def report_contiguous_dates(failed: pd.DataFrame, succeeded: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(data={'day_no': range(0,365)})
    df['day'] = pd.date_range(start='1/1/2019', end='12/31/2019')
    df1 = ( df
           .merge(succeeded, how='left', left_on='day', right_on='success_date')
           .merge(failed, how='left', left_on='day', right_on='fail_date')
          )
    df1['success_date'] = np.where(df1['success_date'].isna(),'','succeeded')
    df1['fail_date'] = np.where(df1['fail_date'].isna(),'','failed')
    df1['rnk'] = df1.groupby('success_date',as_index=False)['day'].rank(method='dense')
    df1['group_id'] = df1['day_no'] - df1['rnk']
    df2 = ( df1
           .groupby(['group_id','success_date','fail_date'],as_index=False)
           .agg(start_date=('day','min'), end_date=('day','max'))
          )
    success = ( df2[df2['success_date']=='succeeded'][['success_date','start_date','end_date']]
               .rename(columns={'success_date':'period_state'})
              )
    failure = ( df2[df2['fail_date']=='failed'][['fail_date','start_date','end_date']]
               .rename(columns={'fail_date':'period_state'})
              )
    return pd.concat([success, failure]).sort_values('start_date')

