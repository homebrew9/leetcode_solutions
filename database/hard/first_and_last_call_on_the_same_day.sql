-- Oracle
/* Write your PL/SQL query statement below */
with t (user1_id, user2_id, call_time, drnk, drnk1) as (
select x.caller_id as user1_id, x.recipient_id as user2_id, x.call_time,
       dense_rank() over (partition by x.caller_id, trunc(x.call_time) order by x.call_time) as drnk,
       dense_rank() over (partition by x.caller_id, trunc(x.call_time) order by x.call_time desc) as drnk1
from (select caller_id, recipient_id, call_time from calls
      union all
      select recipient_id, caller_id, call_time from calls
     ) x
)
select distinct user1_id as user_id
from t
where (drnk = 1 or drnk1 = 1)
group by user1_id, trunc(call_time)
having count(distinct user2_id) = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user1_id, user2_id, call_time, drnk, drnk1) as (
select x.caller_id as user1_id, x.recipient_id as user2_id, x.call_time,
       dense_rank() over (partition by x.caller_id, DATE_TRUNC('DAY', x.call_time) order by x.call_time) as drnk,
       dense_rank() over (partition by x.caller_id, DATE_TRUNC('DAY', x.call_time) order by x.call_time desc) as drnk1
from (select caller_id, recipient_id, call_time from calls
      union all
      select recipient_id, caller_id, call_time from calls
     ) x
)
select distinct user1_id as user_id
from t
where (drnk = 1 or drnk1 = 1)
group by user1_id, DATE_TRUNC('DAY', call_time)
having count(distinct user2_id) = 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user1_id, user2_id, call_time, drnk, drnk1) as (
select x.caller_id as user1_id, x.recipient_id as user2_id, x.call_time,
       dense_rank() over (partition by x.caller_id, CONVERT(DATE, x.call_time) order by x.call_time) as drnk,
       dense_rank() over (partition by x.caller_id, CONVERT(DATE, x.call_time) order by x.call_time desc) as drnk1
from (select caller_id, recipient_id, call_time from calls
      union all
      select recipient_id, caller_id, call_time from calls
     ) x
)
select distinct user1_id as user_id
from t
where (drnk = 1 or drnk1 = 1)
group by user1_id, CONVERT(DATE, call_time)
having count(distinct user2_id) = 1
;


# MySQL
# Write your MySQL query statement below
# Use DATE(dt) or DATE_FORMAT(dt, fmt) to truncate date to day
with t (user1_id, user2_id, call_time, drnk, drnk1) as (
select x.caller_id as user1_id, x.recipient_id as user2_id, x.call_time,
       dense_rank() over (partition by x.caller_id, DATE_FORMAT(x.call_time, '%Y-%m-%d') order by x.call_time) as drnk,
       dense_rank() over (partition by x.caller_id, DATE_FORMAT(x.call_time, '%Y-%m-%d') order by x.call_time desc) as drnk1
from (select caller_id, recipient_id, call_time from calls
      union all
      select recipient_id, caller_id, call_time from calls
     ) x
)
select distinct user1_id as user_id
from t
where (drnk = 1 or drnk1 = 1)
group by user1_id, DATE_FORMAT(call_time, '%Y-%m-%d')
having count(distinct user2_id) = 1
;


# Pandas
import pandas as pd

def same_day_calls(calls: pd.DataFrame) -> pd.DataFrame:
    calls = calls.rename(columns={'caller_id':'user1_id', 'recipient_id':'user2_id'})
    calls_rev = calls[['user2_id','user1_id','call_time']]
    calls_rev = calls_rev.rename(columns={'user1_id':'user2_id', 'user2_id':'user1_id'})
    df = pd.concat([calls, calls_rev])
    df['call_day'] = df['call_time'].dt.strftime('%Y-%m-%d')
    df1 = df.assign(rnk1=df.groupby(['user1_id','call_day'])['call_time'].rank(method='dense'),
                    rnk2=df.groupby(['user1_id','call_day'])['call_time'].rank(method='dense',ascending=False)
                )
    first_call = df1.query('rnk1==1')[['user1_id','user2_id','call_day']]
    last_call = df1.query('rnk2==1')[['user1_id','user2_id','call_day']]
    return ( first_call
            .merge(last_call, how='inner', on=['user1_id','call_day'])
            .query('user2_id_x==user2_id_y')[['user1_id']]
            .drop_duplicates()
            .rename(columns={'user1_id':'user_id'})
           )

