-- Oracle
/* Write your PL/SQL query statement below */
select t1.team_name as home_team,
       t2.team_name as away_team
from teams t1
     cross join teams t2
where t1.team_name != t2.team_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select t1.team_name as home_team,
       t2.team_name as away_team
from teams t1
     cross join teams t2
where t1.team_name != t2.team_name
;


-- SQL Server
/* Write your T-SQL query statement below */
select t1.team_name as home_team,
       t2.team_name as away_team
from teams t1
     cross join teams t2
where t1.team_name != t2.team_name
;


# MySQL
# Write your MySQL query statement below
select t1.team_name as home_team,
       t2.team_name as away_team
from teams t1
     cross join teams t2
where t1.team_name != t2.team_name
;


# Pandas
import pandas as pd

def find_all_matches(teams: pd.DataFrame) -> pd.DataFrame:
    return (  teams.merge(teams, how='cross')
                   .query('team_name_x != team_name_y')
                   .rename(columns={'team_name_x':'home_team', 'team_name_y':'away_team'})
           )

