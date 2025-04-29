-- Oracle
/* Write your PL/SQL query statement below */
select team_id, team_name, 3 * wins + draws as points,
       rank() over (order by 3 * wins + draws desc) as position
  from teamstats
 order by points desc, team_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select team_id, team_name, 3 * wins + draws as points,
       rank() over (order by 3 * wins + draws desc) as position
  from teamstats
 order by points desc, team_name
;


-- SQL Server
/* Write your T-SQL query statement below */
select team_id, team_name, 3 * wins + draws as points,
       rank() over (order by 3 * wins + draws desc) as position
  from teamstats
 order by points desc, team_name
;


# MySQL
# Write your MySQL query statement below
select team_id, team_name, 3 * wins + draws as points,
       rank() over (order by 3 * wins + draws desc) as position
  from teamstats
 order by points desc, team_name
;


# Pandas
import pandas as pd

def calculate_team_standings(team_stats: pd.DataFrame) -> pd.DataFrame:
    team_stats['points'] = 3 * team_stats['wins'] + team_stats['draws']
    team_stats['position'] = team_stats['points'].rank(method='min', ascending=False)
    return ( team_stats[['team_id','team_name','points','position']]
            .sort_values(by=['points', 'team_name'], ascending=[False, True])
           )

