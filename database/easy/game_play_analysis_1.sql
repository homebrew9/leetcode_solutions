-- Oracle
/* Write your PL/SQL query statement below */
select player_id, to_char(min(event_date), 'yyyy-mm-dd') as first_login
  from activity
 group by player_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select player_id, min(event_date) as first_login
from activity
group by player_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select player_id as "player_id",
       convert(varchar, min(event_date), 23) as "first_login"
from activity
group by player_id
;


# MySQL
# Write your MySQL query statement below
select player_id, min(event_date) as first_login
from activity
group by player_id
;


# Pandas
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return (  activity
              .assign( rnk=activity.sort_values(['event_date'])
                       .groupby(['player_id'])
                       .cumcount() + 1
                     )
              .query('rnk == 1')[['player_id','event_date']]
              .rename(columns={'event_date': 'first_login'})
           )

