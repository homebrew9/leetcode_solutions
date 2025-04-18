-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, time_stamp, action, time_diff) as (
select user_id, time_stamp, action,
       time_stamp - lag(time_stamp) over (partition by user_id order by time_stamp) as time_diff
from confirmations
)
select distinct user_id
from t
where time_diff <= 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, time_stamp, action, time_diff) as (
select user_id, time_stamp, action,
       time_stamp - lag(time_stamp) over (partition by user_id order by time_stamp) as time_diff
from confirmations
)
select distinct user_id
from t
where time_diff <= interval '1 DAY'
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, time_stamp, action, time_diff) as (
select user_id, time_stamp, action,
       time_stamp - lag(time_stamp) over (partition by user_id order by time_stamp) as time_diff
from confirmations
)
select distinct user_id
from t
where time_diff <= 1
;


# MySQL
# Write your MySQL query statement below
with t (user_id, time_stamp, action, seconds) as (
select user_id, time_stamp, action,
       timestampdiff(second, lag(time_stamp) over (partition by user_id order by time_stamp), time_stamp) as seconds
from confirmations
)
select distinct user_id
from t
where seconds <= 24 * 60 * 60
;


# Pandas
import pandas as pd

def find_requesting_users(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    # Sort by user_id and time_stamp first, so that shift() works correctly
    confirmations = confirmations.sort_values(by=['user_id','time_stamp'])
    
    # Add the lag value partitioned by user_id
    confirmations['lag'] = confirmations.groupby('user_id',as_index=False)['time_stamp'].shift(1)
    
    # Calculate diff in seconds, NaTs in the expresson result in NaTs, which is okay
    confirmations['diff_in_seconds'] = (confirmations['time_stamp'] - confirmations['lag'])/pd.Timedelta(seconds=1)
    
    # Fetch distinct user_ids whose diff in seconds is less than 1 day equivalent
    return confirmations[confirmations['diff_in_seconds']<=24*60*60][['user_id']].drop_duplicates()

