-- Oracle
/* Write your PL/SQL query statement below */
select player_id, to_char(event_date, 'YYYY-MM-DD') as event_date,
       sum(games_played) over (partition by player_id order by event_date) as games_played_so_far
  from activity
;


-- PostgreSQL
/*
# The MySQL query works for PostgreSQL as well.
# Not sure why PostgreSQL is absent as an option for this problem.

with activity (player_id, device_id, event_date, games_played) as (
    select 1, 2, '2016-03-01'::date, 5 union all
    select 1, 2, '2016-05-02'::date, 6 union all
    select 1, 3, '2017-06-25'::date, 1 union all
    select 3, 1, '2016-03-02'::date, 0 union all
    select 3, 4, '2018-07-03'::date, 5
)
select player_id,
       event_date,
       sum(games_played) over (partition by player_id order by event_date) as games_played_so_far
  from activity
;
*/


-- SQL Server
/* Write your T-SQL query statement below */
select player_id, event_date,
       sum(games_played) over (partition by player_id order by event_date) as games_played_so_far
from activity
;


# MySQL
# Write your MySQL query statement below
select player_id,
       event_date,
       sum(games_played) over (partition by player_id order by event_date) as games_played_so_far
  from activity
;

# Write your MySQL query statement below
select player_id,
       event_date,
       sum(games_played) over (partition by player_id
                               order by event_date
                               rows between unbounded preceding and current row
                              ) as games_played_so_far
  from activity
;


# Pandas
import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return (  activity.assign(
                  games_played_so_far=activity.sort_values(['player_id','event_date'])
                                              .groupby(['player_id'])['games_played']
                                              .cumsum()
              )[['player_id','event_date','games_played_so_far']]
           )

