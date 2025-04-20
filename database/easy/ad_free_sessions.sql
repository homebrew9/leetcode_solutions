-- Oracle
/* Write your PL/SQL query statement below */
select p.session_id
  from playback p
 where p.session_id not in (
    select p1.session_id
      from playback p1
           inner join ads a on (a.customer_id = p1.customer_id and
                                a.timestamp between p1.start_time and p1.end_time)
)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.session_id
  from playback p
 where p.session_id not in (
    select p1.session_id
      from playback p1
           inner join ads a on (a.customer_id = p1.customer_id and
                                a.timestamp between p1.start_time and p1.end_time)
)
;


-- SQL Server
/* Write your T-SQL query statement below */
select p.session_id
  from playback p
 where p.session_id not in (
    select p1.session_id
      from playback p1
           inner join ads a on (a.customer_id = p1.customer_id and
                                a.timestamp between p1.start_time and p1.end_time)
)
;


# MySQL
# Write your MySQL query statement below
select p.session_id
  from playback p
 where p.session_id not in (
    select p1.session_id
      from playback p1
           inner join ads a on (a.customer_id = p1.customer_id and
                                a.timestamp between p1.start_time and p1.end_time)
)
;


# Pandas
import pandas as pd

def ad_free_sessions(playback: pd.DataFrame, ads: pd.DataFrame) -> pd.DataFrame:
    sessions_with_ads = (  playback.merge(ads, how='inner', on='customer_id')
                                   .query('timestamp >= start_time and timestamp <= end_time')['session_id']
                        )
    return playback[~playback['session_id'].isin(sessions_with_ads)][['session_id']]
    
