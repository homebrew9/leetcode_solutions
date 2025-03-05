-- Oracle
/* Write your PL/SQL query statement below */
with player_streak (player_id, streak) as (
select distinct player_id, 0
from matches
),
t as (
select player_id, match_day, result,
       case when result != coalesce(lag(result) over (partition by player_id order by match_day), 'X')
            then 1
            else 0
       end as result_change
from matches
),
t1 as (
select player_id, match_day, result, result_change,
       sum(result_change) over (order by player_id, match_day rows between unbounded preceding and current row) as group_id
from t
),
t2 as (
select player_id, result, count(*) as streak
from t1
group by player_id, group_id, result
),
t3 as (
select distinct x.player_id, x.result, x.streak
from t2 x
where x.result = 'Win'
and x.streak = (select max(y.streak) from t2 y where y.player_id = x.player_id and y.result = 'Win')
)
select ps.player_id, coalesce(t3.streak, ps.streak) as longest_streak
from player_streak ps
     left outer join t3 on (t3.player_id = ps.player_id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with player_streak (player_id, streak) as (
select distinct player_id, 0
from matches
),
t as (
select player_id, match_day, result,
       case when result != coalesce(lag(result) over (partition by player_id order by match_day), 'X')
            then 1
            else 0
       end as result_change
from matches
),
t1 as (
select player_id, match_day, result, result_change,
       sum(result_change) over (order by player_id, match_day rows between unbounded preceding and current row) as group_id
from t
),
t2 as (
select player_id, result, count(*) as streak
from t1
group by player_id, group_id, result
),
t3 as (
select distinct x.player_id, x.result, x.streak
from t2 x
where x.result = 'Win'
and x.streak = (select max(y.streak) from t2 y where y.player_id = x.player_id and y.result = 'Win')
)
select ps.player_id, coalesce(t3.streak, ps.streak) as longest_streak
from player_streak ps
     left outer join t3 on (t3.player_id = ps.player_id)
;


-- SQL Server
/* Write your T-SQL query statement below */
with player_streak (player_id, streak) as (
select distinct player_id, 0
from matches
),
t as (
select player_id, match_day, result,
       case when result != coalesce(lag(result) over (partition by player_id order by match_day), 'X')
            then 1
            else 0
       end as result_change
from matches
),
t1 as (
select player_id, match_day, result, result_change,
       sum(result_change) over (order by player_id, match_day rows between unbounded preceding and current row) as group_id
from t
),
t2 as (
select player_id, result, count(*) as streak
from t1
group by player_id, group_id, result
),
t3 as (
select distinct x.player_id, x.result, x.streak
from t2 x
where x.result = 'Win'
and x.streak = (select max(y.streak) from t2 y where y.player_id = x.player_id and y.result = 'Win')
)
select ps.player_id, coalesce(t3.streak, ps.streak) as longest_streak
from player_streak ps
     left outer join t3 on (t3.player_id = ps.player_id)
;


# MySQL
# Write your MySQL query statement below
with player_streak (player_id, streak) as (
select distinct player_id, 0
from matches
),
t as (
select player_id, match_day, result,
       case when result != coalesce(lag(result) over (partition by player_id order by match_day), 'X')
            then 1
            else 0
       end as result_change
from matches
),
t1 as (
select player_id, match_day, result, result_change,
       sum(result_change) over (order by player_id, match_day rows between unbounded preceding and current row) as group_id
from t
),
t2 as (
select player_id, result, count(*) as streak
from t1
group by player_id, group_id, result
),
t3 as (
select distinct x.player_id, x.result, x.streak
from t2 x
where x.result = 'Win'
and x.streak = (select max(y.streak) from t2 y where y.player_id = x.player_id and y.result = 'Win')
)
select ps.player_id, coalesce(t3.streak, ps.streak) as longest_streak
from player_streak ps
     left outer join t3 on (t3.player_id = ps.player_id)
;


# Pandas
import pandas as pd

def longest_winning_streak(matches: pd.DataFrame) -> pd.DataFrame:
    matches.sort_values(['player_id','match_day'],inplace=True)
    matches['chg'] = np.where(matches.shift(1)['result'] != matches['result'],1,0)
    matches['group_id'] = matches['chg'].cumsum()
    df = ( matches
          .groupby(['player_id','group_id','result'],as_index=False)['match_day']
          .count()
          .query('result=="Win"')
          .rename(columns={'match_day':'streak'})
         )
    df = ( df
          .groupby('player_id',as_index=False)['streak']
          .max()
          .rename(columns={'streak': 'longest_streak'})
         )
    return ( matches[['player_id']]
            .drop_duplicates()
            .merge(df,how='left',on='player_id')
            .fillna(0)
           )

