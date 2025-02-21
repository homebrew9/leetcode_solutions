-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select user_id, session_start, session_end, session_id, session_type,
           lag(session_end) over (partition by user_id, session_type order by session_start) as prev_session_end,
           lag(session_type) over (partition by user_id, session_type order by session_start) as prev_session_type,
           (session_start - lag(session_end) over (partition by user_id, session_type order by session_start)) * 24 as diff_hours
      from sessions
)
select distinct user_id
  from t
 where diff_hours <= 12
 order by user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select user_id, session_start, session_end, session_id, session_type,
           lag(session_end) over (partition by user_id, session_type order by session_start) as prev_session_end,
           lag(session_type) over (partition by user_id, session_type order by session_start) as prev_session_type,
           extract(
               epoch from
                   session_start
                   -
                   lag(session_end) over (partition by user_id, session_type order by session_start)
           ) / 60 / 60 as diff_hours
      from sessions
)
select distinct user_id
  from t
 where diff_hours <= 12
 order by user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select user_id, session_start, session_end, session_id, session_type,
           lag(session_end) over (partition by user_id, session_type order by session_start) as prev_session_end,
           lag(session_type) over (partition by user_id, session_type order by session_start) as prev_session_type,
           DATEDIFF(hour, 
                    lag(session_end) over (partition by user_id, session_type order by session_start),
                    session_start
                   ) as diff_hours
      from sessions
)
select distinct user_id
  from t
 where diff_hours <= 12
 order by user_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select user_id, session_start, session_end, session_id, session_type,
           lag(session_end) over (partition by user_id, session_type order by session_start) as prev_session_end,
           lag(session_type) over (partition by user_id, session_type order by session_start) as prev_session_type,
           TIMESTAMPDIFF(hour, 
                         lag(session_end) over (partition by user_id, session_type order by session_start),
                         session_start
                        ) as diff_hours
      from sessions
)
select distinct user_id
  from t
 where diff_hours <= 12
 order by user_id
;


# Pandas
import pandas as pd

def user_activities(sessions: pd.DataFrame) -> pd.DataFrame:
    return ( sessions
            .merge(sessions, how='inner', on=['user_id','session_type'])
            .query(
                    'session_start_y > session_start_x & (session_start_y - session_end_x).dt.total_seconds()/60/60 < 12'
                  )[['user_id']]
            .drop_duplicates()
            .sort_values('user_id')
           )

