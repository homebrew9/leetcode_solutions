-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select team_name, 3 * wins + draws as points
      from TeamStats
),
t1 as (
select team_name, points,
       rank() over (order by points desc) as position
  from t
)
select team_name, points, position,
       case when position < 0.33 * max(position) over () + 1 then 'Tier 1'
            when position < 0.66 * max(position) over () + 1 then 'Tier 2'
            else 'Tier 3'
       end as tier
  from t1
 order by points desc, team_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select team_name, 3 * wins + draws as points
      from TeamStats
),
t1 as (
select team_name, points,
       rank() over (order by points desc) as position
  from t
)
select team_name, points, position,
       case when position < 0.33 * max(position) over () + 1 then 'Tier 1'
            when position < 0.66 * max(position) over () + 1 then 'Tier 2'
            else 'Tier 3'
       end as tier
  from t1
 order by points desc, team_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select team_name, 3 * wins + draws as points
      from TeamStats
),
t1 as (
select team_name, points,
       rank() over (order by points desc) as position
  from t
)
select team_name, points, position,
       case when position < 0.33 * max(position) over () + 1 then 'Tier 1'
            when position < 0.66 * max(position) over () + 1 then 'Tier 2'
            else 'Tier 3'
       end as tier
  from t1
 order by points desc, team_name
;


# MySQL
# Write your MySQL query statement below
with t as (
    select team_name, 3 * wins + draws as points
      from TeamStats
),
t1 as (
select team_name, points,
       rank() over (order by points desc) as position
  from t
)
select team_name, points, position,
       case when position < 0.33 * max(position) over () + 1 then 'Tier 1'
            when position < 0.66 * max(position) over () + 1 then 'Tier 2'
            else 'Tier 3'
       end as tier
  from t1
 order by points desc, team_name
;


# Pandas
import pandas as pd

def calculate_team_tiers(team_stats: pd.DataFrame) -> pd.DataFrame:
    team_stats['points'] = 3 * team_stats['wins'] + team_stats['draws']
    team_stats['position'] = team_stats['points'].rank(method='min', ascending=False)
    max_position = team_stats['position'].max()
    team_stats['tier'] = np.where(team_stats['position'] < 0.33 * max_position + 1,
                                  'Tier 1',
                                  np.where(team_stats['position'] < 0.66 * max_position + 1,
                                           'Tier 2',
                                           'Tier 3'
                                          )
                                 )
    return ( team_stats[['team_name','points','position','tier']]
            .sort_values(by=['points','team_name'], ascending=[0,1])
           )

