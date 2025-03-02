-- Oracle
/* Write your PL/SQL query statement below */
with t (player_id, install_date) as (
select x.player_id, x.event_date as install_date
from activity x
where x.event_date = (
                        select min(y.event_date)
                        from activity y
                        where y.player_id = x.player_id
                     )
)
select to_char(t.install_date, 'YYYY-MM-DD') as install_dt,
       count(t.player_id) as installs,
       round(count(a.player_id) / count(t.player_id), 2) as day1_retention
from t
     left outer join activity a on (a.player_id = t.player_id and a.event_date = t.install_date + 1)
group by t.install_date
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (player_id, install_date) as (
select x.player_id, x.event_date as install_date
from activity x
where x.event_date = (
                        select min(y.event_date)
                        from activity y
                        where y.player_id = x.player_id
                     )
)
select to_char(t.install_date, 'YYYY-MM-DD') as install_dt,
       count(t.player_id) as installs,
       round(count(a.player_id)::numeric / count(t.player_id)::numeric, 2) as day1_retention
from t
     left outer join activity a on (a.player_id = t.player_id and a.event_date = t.install_date + 1)
group by t.install_date
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (player_id, install_date) as (
select x.player_id, x.event_date as install_date
from activity x
where x.event_date = (
                        select min(y.event_date)
                        from activity y
                        where y.player_id = x.player_id
                     )
)
select t.install_date as install_dt,
       count(t.player_id) as installs,
       ROUND(CONVERT(FLOAT, count(a.player_id)) / CONVERT(FLOAT, count(t.player_id)), 2) as day1_retention
from t
     left outer join activity a on (a.player_id = t.player_id and a.event_date = DATEADD(DAY, 1, t.install_date))
group by t.install_date
;


# MySQL
# Write your MySQL query statement below
with t (player_id, install_date) as (
select player_id, min(event_date) as install_date
from activity
group by player_id
)
select t.install_date as install_dt,
       count(t.player_id) as installs,
       round(count(a.player_id) / count(t.player_id), 2) as day1_retention
from t
     left outer join activity a on (a.player_id = t.player_id and a.event_date = t.install_date + 1)
group by t.install_date
;


# Pandas
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['next_day'] = activity['event_date'] + pd.Timedelta(days=1)
    df = ( activity
          .assign(rnk=activity.groupby('player_id')['event_date'].rank(method='dense'))
          .query('rnk==1')[['player_id','event_date','next_day']]
         )
    df1 = df.merge(activity,how='left',left_on=['player_id','next_day'],right_on=['player_id','event_date'])
    df2 = ( df1
           .groupby('event_date_x',as_index=False)
           .agg(installs=('next_day_x','count'), next_day_count=('event_date_y','count'))
          )
    # Note that Python rounds to the nearest EVEN number! Eg. round(0.125,2) = 0.12
    # Hence we use: math.floor(n * 100 + 0.5) / 100 to get 0.13 from n = 0.125
    df2['Day1_retention'] =  ((df2['next_day_count']/df2['installs'])*100+0.5).apply(np.floor)/100
    return df2[['event_date_x','installs','Day1_retention']].rename(columns={'event_date_x':'install_dt'})

