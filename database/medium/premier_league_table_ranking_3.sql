-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select season_id, team_id, team_name,
           3*wins + draws as points,
           goals_for-goals_against as goal_difference
      from seasonstats
),
t1 as (
    select season_id, team_id, team_name, points, goal_difference,
           dense_rank() over (partition by season_id
                              order by points desc, goal_difference desc, team_name) as position
      from t
)
select season_id, team_id, team_name, points, goal_difference, position
  from t1
 order by season_id, position, team_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select season_id, team_id, team_name,
           3*wins + draws as points,
           goals_for-goals_against as goal_difference
      from seasonstats
),
t1 as (
    select season_id, team_id, team_name, points, goal_difference,
           dense_rank() over (partition by season_id
                              order by points desc, goal_difference desc, team_name) as position
      from t
)
select season_id, team_id, team_name, points, goal_difference, position
  from t1
 order by season_id, position, team_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select season_id, team_id, team_name,
           3*wins + draws as points,
           goals_for-goals_against as goal_difference
      from seasonstats
),
t1 as (
    select season_id, team_id, team_name, points, goal_difference,
           dense_rank() over (partition by season_id
                              order by points desc, goal_difference desc, team_name) as position
      from t
)
select season_id, team_id, team_name, points, goal_difference, position
  from t1
 order by season_id, position, team_name
;


# MySQL
# Write your MySQL query statement below
with t as (
    select season_id, team_id, team_name,
           3*wins + draws as points,
           goals_for-goals_against as goal_difference
      from seasonstats
),
t1 as (
    select season_id, team_id, team_name, points, goal_difference,
           dense_rank() over (partition by season_id
                              order by points desc, goal_difference desc, team_name) as position
      from t
)
select season_id, team_id, team_name, points, goal_difference, position
  from t1
 order by season_id, position, team_name
;


# Pandas
import pandas as pd

def process_team_standings(season_stats: pd.DataFrame) -> pd.DataFrame:
    season_stats['points'] = season_stats['wins'] * 3 + season_stats['draws']
    season_stats['goal_difference'] = season_stats['goals_for'] - season_stats['goals_against']
    season_stats['position'] = ( season_stats
                                .sort_values(by=['season_id','points','goal_difference'], ascending=[True,False,False])
                                .groupby('season_id', as_index=0)
                                .cumcount()
                                .add(1)
                               )
    return ( season_stats[['season_id','team_id','team_name','points','goal_difference','position']]
            .sort_values(['season_id','position','team_name'])
           )

