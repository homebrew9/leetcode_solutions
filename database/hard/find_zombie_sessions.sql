-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select session_id, user_id,
           (max(event_timestamp) - min(event_timestamp)) * 24 * 60 as session_duration_minutes,
           sum(case when event_type = 'scroll' then 1 else 0 end) as scroll_count,
           sum(case when event_type = 'click' then 1 else 0 end) as click_count,
           sum(case when event_type = 'purchase' then 1 else 0 end) as purchase_count
      from app_events
     group by session_id, user_id
)
select session_id, user_id, session_duration_minutes, scroll_count
  from t
 where session_duration_minutes > 30
   and scroll_count >= 5
   and click_count / scroll_count < 0.2
   and purchase_count = 0
 order by scroll_count desc, session_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select session_id, user_id,
           EXTRACT(EPOCH FROM max(event_timestamp) - min(event_timestamp)) / 60 as session_duration_minutes,
           sum(case when event_type = 'scroll' then 1 else 0 end) as scroll_count,
           sum(case when event_type = 'click' then 1 else 0 end) as click_count,
           sum(case when event_type = 'purchase' then 1 else 0 end) as purchase_count
      from app_events
     group by session_id, user_id
)
select session_id, user_id, session_duration_minutes, scroll_count
  from t
 where session_duration_minutes > 30
   and scroll_count >= 5
   and click_count::NUMERIC / scroll_count < 0.2
   and purchase_count = 0
 order by scroll_count desc, session_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select session_id, user_id,
           DATEDIFF(SECOND, min(event_timestamp), max(event_timestamp)) / 60.0 as session_duration_minutes,
           sum(case when event_type = 'scroll' then 1 else 0 end) as scroll_count,
           sum(case when event_type = 'click' then 1 else 0 end) as click_count,
           sum(case when event_type = 'purchase' then 1 else 0 end) as purchase_count
      from app_events
     group by session_id, user_id
)
select session_id, user_id, session_duration_minutes, scroll_count
  from t
 where session_duration_minutes > 30
   and scroll_count >= 5
   and CONVERT(NUMERIC, click_count) / scroll_count < 0.2
   and purchase_count = 0
 order by scroll_count desc, session_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select session_id, user_id,
           TIMESTAMPDIFF(SECOND, min(event_timestamp), max(event_timestamp)) / 60 as session_duration_minutes,
           sum(case when event_type = 'scroll' then 1 else 0 end) as scroll_count,
           sum(case when event_type = 'click' then 1 else 0 end) as click_count,
           sum(case when event_type = 'purchase' then 1 else 0 end) as purchase_count
      from app_events
     group by session_id, user_id
)
select session_id, user_id, session_duration_minutes, scroll_count
  from t
 where session_duration_minutes > 30
   and scroll_count >= 5
   and click_count / scroll_count < 0.2
   and purchase_count = 0
 order by scroll_count desc, session_id
;


# Pandas
import pandas as pd

def find_zombie_sessions(app_events: pd.DataFrame) -> pd.DataFrame:
    app_events['event_timestamp'] = pd.to_datetime(app_events['event_timestamp'])
    app_events['is_scroll'] = app_events['event_type'] == 'scroll'
    app_events['is_click'] = app_events['event_type'] == 'click'
    app_events['is_purchase'] = app_events['event_type'] == 'purchase'
    df = ( app_events
          .groupby(['session_id','user_id'], as_index=0)
          .agg(min_ts=('event_timestamp','min'),
               max_ts=('event_timestamp','max'),
               scroll_count=('is_scroll','sum'),
               click_count=('is_click','sum'),
               purchase_count=('is_purchase','sum')
              )
         )
    df['session_duration_minutes'] = (df['max_ts'] - df['min_ts']).dt.total_seconds()/60
    df1 = ( df
           .query('session_duration_minutes > 30 and scroll_count >= 5 and click_count / scroll_count < 0.2 and purchase_count == 0')
           .sort_values(by=['scroll_count','session_id'], ascending=[False,True])[['session_id','user_id','session_duration_minutes','scroll_count']]
          )
    return df1






















