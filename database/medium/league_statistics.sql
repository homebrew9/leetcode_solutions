-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


# MySQL
# Write your MySQL query statement below
with t as (
select home_team_id as team_id, away_team_id as opponent_id,
       home_team_goals as goal_for, away_team_goals as goal_against,
       case when home_team_goals > away_team_goals then 3
            when home_team_goals < away_team_goals then 0
            else 1
       end as points
from matches
union all
select away_team_id as team_id, home_team_id as opponent_id,
       away_team_goals as goal_for, home_team_goals as goal_against,
       case when away_team_goals > home_team_goals then 3
            when away_team_goals < home_team_goals then 0
            else 1
       end as points
from matches
)
select x.team_name, count(t.opponent_id) as matches_played,
       sum(t.points) as points,
       sum(t.goal_for) as goal_for,
       sum(t.goal_against) as goal_against,
       sum(t.goal_for) - sum(t.goal_against) as goal_diff
from t
     inner join teams x on (x.team_id = t.team_id)
group by x.team_name
order by points desc, goal_diff desc, team_name
;


# Pandas
import pandas as pd

def league_statistics(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    matches['home_team_points'] = ( np.where(matches['home_team_goals'] > matches['away_team_goals'],
                                    3,
                                    np.where(matches['home_team_goals'] < matches['away_team_goals'], 0, 1))
                                  )
    matches['away_team_points'] = ( np.where(matches['away_team_goals'] > matches['home_team_goals'],
                                    3,
                                    np.where(matches['away_team_goals'] < matches['home_team_goals'], 0, 1))
                                  )
    df1 = ( matches
           .groupby('home_team_id', as_index=0)
           .agg({'away_team_id':'count', 'home_team_goals':'sum', 'away_team_goals':'sum', 'home_team_points':'sum'})
           .rename(columns={'home_team_id':'team_id', 'away_team_id':'matches_played',
                            'home_team_goals':'goal_for', 'away_team_goals':'goal_against',
                            'home_team_points': 'points'})
          )
    df2 = ( matches
           .groupby('away_team_id', as_index=0)
           .agg({'home_team_id':'count', 'home_team_goals':'sum', 'away_team_goals':'sum', 'away_team_points':'sum'})
           .rename(columns={'away_team_id':'team_id', 'home_team_id':'matches_played',
                            'home_team_goals':'goal_against', 'away_team_goals':'goal_for',
                            'away_team_points': 'points'})
          )
    df = ( pd
          .concat([df1, df2])
          .groupby('team_id', as_index=0)
          .agg({'matches_played':'sum', 'goal_for':'sum', 'goal_against':'sum', 'points':'sum'})
          .merge(teams, how='inner', on='team_id')[['team_name','matches_played','points','goal_for','goal_against']]
         )
    df['goal_diff'] = df['goal_for'] - df['goal_against']
    return df.sort_values(by=['points', 'goal_diff', 'team_name'], ascending=[False, False, True])

