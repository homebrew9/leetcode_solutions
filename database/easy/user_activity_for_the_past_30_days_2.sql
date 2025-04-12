-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select user_id, count(distinct session_id) as distinct_sessions
      from activity
     where activity_date between DATE'2019-07-27' - 30 + 1 and DATE'2019-07-27'
     group by user_id
)
select round(coalesce(sum(distinct_sessions) / count(*), 0), 2) as average_sessions_per_user
  from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select user_id, count(distinct session_id) as distinct_sessions
      from activity
     where activity_date between DATE'2019-07-27' - 30 + 1 and DATE'2019-07-27'
     group by user_id
)
select round(coalesce(sum(distinct_sessions) / count(*), 0), 2) as average_sessions_per_user
  from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select user_id, convert(float, count(distinct session_id)) as distinct_sessions
      from activity
     where activity_date between DATEADD(DAY, -29, '2019-07-27') and '2019-07-27'
     group by user_id
)
select round(coalesce(sum(distinct_sessions) / count(*), 0), 2) as average_sessions_per_user
  from t
;


# MySQL
# Write your MySQL query statement below
with t as (
    select user_id, count(distinct session_id) as distinct_sessions
      from activity
     where activity_date between DATE_SUB('2019-07-27', INTERVAL '29' DAY) and '2019-07-27'
     group by user_id
)
select coalesce(round(sum(distinct_sessions) / count(*), 2), 0) as average_sessions_per_user
  from t
;


# Pandas
import pandas as pd
from datetime import datetime, timedelta

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    start_date = datetime(2019,7,27) - timedelta(days=29)
    end_date = datetime(2019,7,27)
    df = ( activity[
                      (activity['activity_date'] >= start_date)
                      &
                      (activity['activity_date'] <= end_date)
                   ][['user_id','session_id']]
          .drop_duplicates()
          .groupby('user_id',as_index=0)['session_id']
          .count()
         )
    avg_sess_per_user = np.where(len(df) == 0, 0, round(df['session_id'].sum()/len(df),2))
    return pd.DataFrame(data={'average_sessions_per_user': avg_sess_per_user}, index=[0])

