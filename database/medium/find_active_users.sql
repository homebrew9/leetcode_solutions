-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, created_at, prev_dt, next_dt) as (
select user_id, created_at,
       lag(created_at) over (partition by user_id order by created_at) as prev_dt,
       lead(created_at) over (partition by user_id order by created_at) as next_dt
from users
)
select distinct user_id
from t
where (abs(created_at - next_dt) <= 7 or abs(created_at - prev_dt) <= 7)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, created_at, prev_dt, next_dt) as (
select user_id, created_at,
       lag(created_at) over (partition by user_id order by created_at) as prev_dt,
       lead(created_at) over (partition by user_id order by created_at) as next_dt
from users
)
select distinct user_id
from t
where (abs(created_at - next_dt) <= 7 or abs(created_at - prev_dt) <= 7)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, created_at, prev_dt, next_dt) as (
select user_id, created_at,
       lag(created_at) over (partition by user_id order by created_at) as prev_dt,
       lead(created_at) over (partition by user_id order by created_at) as next_dt
from users
)
select distinct user_id
from t
where ABS(DATEDIFF(DAY, created_at, next_dt)) <= 7 or ABS(DATEDIFF(DAY, created_at, prev_dt)) <= 7
;


# MySQL
# Write your MySQL query statement below
with t (user_id, created_at, prev_dt, next_dt) as (
select user_id, created_at,
       lag(created_at) over (partition by user_id order by created_at) as prev_dt,
       lead(created_at) over (partition by user_id order by created_at) as next_dt
from users
)
select distinct user_id
from t
where (abs(created_at - next_dt) <= 7 or abs(created_at - prev_dt) <= 7)
;


# Pandas
import pandas as pd

def find_active_users(users: pd.DataFrame) -> pd.DataFrame:
    users = users.sort_values(['user_id','created_at'])
    df = ( pd
          .concat([ users,
                    users
                   .shift(1)[['user_id','created_at']]
                   .rename(columns={'user_id':'prev_user_id', 'created_at':'prev_dt'})
                  ],
                  axis=1
                 )
         )
    df['date_diff'] = (df['created_at'] - df['prev_dt']).dt.days
    return df.query('user_id == prev_user_id and date_diff <= 7')[['user_id']].drop_duplicates()

