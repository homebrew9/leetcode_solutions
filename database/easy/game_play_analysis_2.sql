-- Oracle
/* Write your PL/SQL query statement below */
select a.player_id, a.device_id
  from activity a
 where a.event_date = (select min(a1.event_date)
                         from activity a1
                        where a1.player_id = a.player_id
                      )
;


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
with t (player_id, first_login) as (
    select player_id, min(event_date)
      from activity
     group by player_id
)
select a.player_id, a.device_id
  from activity a
       inner join t on (t.player_id = a.player_id and t.first_login = a.event_date)
;


# Pandas
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['rnum'] = activity.groupby(['player_id'])['event_date'].rank(method='first')
    return activity[activity['rnum']==1][['player_id','device_id']]

