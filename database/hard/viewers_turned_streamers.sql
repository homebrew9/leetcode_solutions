-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id) as (
select a.user_id
from sessions a
where a.session_type = 'Viewer'
and a.session_start = (select min(b.session_start) from sessions b where b.user_id = a.user_id)
)
select t.user_id, count(*) as sessions_count
from t
     inner join sessions s on (t.user_id = s.user_id and s.session_type = 'Streamer')
group by t.user_id
order by count(*) desc, t.user_id desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id) as (
select a.user_id
from sessions a
where a.session_type = 'Viewer'
and a.session_start = (select min(b.session_start) from sessions b where b.user_id = a.user_id)
)
select t.user_id, count(*) as sessions_count
from t
     inner join sessions s on (t.user_id = s.user_id and s.session_type = 'Streamer')
group by t.user_id
order by count(*) desc, t.user_id desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id) as (
select a.user_id
from sessions a
where a.session_type = 'Viewer'
and a.session_start = (select min(b.session_start) from sessions b where b.user_id = a.user_id)
)
select t.user_id, count(*) as sessions_count
from t
     inner join sessions s on (t.user_id = s.user_id and s.session_type = 'Streamer')
group by t.user_id
order by count(*) desc, t.user_id desc
;


# MySQL
# Write your MySQL query statement below
with t (user_id) as (
select a.user_id
from sessions a
where a.session_type = 'Viewer'
and a.session_start = (select min(b.session_start) from sessions b where b.user_id = a.user_id)
)
select t.user_id, count(*) as sessions_count
from t
     inner join sessions s on (t.user_id = s.user_id and s.session_type = 'Streamer')
group by t.user_id
order by count(*) desc, t.user_id desc
;


# Pandas
import pandas as pd

def count_turned_streamers(sessions: pd.DataFrame) -> pd.DataFrame:
    first_viewers = ( sessions
                     .assign(rnk=sessions.groupby('user_id')['session_start'].rank(method='dense'))
                     .query('rnk==1 & session_type=="Viewer"')['user_id']
                    )
    return ( sessions[(sessions['user_id'].isin(first_viewers)) & (sessions['session_type']=='Streamer')]
            .groupby('user_id',as_index=False)['session_id']
            .count()
            .rename(columns={'session_id':'sessions_count'})
            .sort_values(by=['sessions_count','user_id'],ascending=[False,False])
           )

