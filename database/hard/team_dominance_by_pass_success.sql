-- Oracle
/* Write your PL/SQL query statement below */
SELECT
    T1.team_name,
    case when time_stamp <= '45:00' then 1 else 2 end AS half_number,
    SUM(case when T1.team_name = T2.team_name then 1 else -1 end) AS dominance
FROM
    Passes
    INNER JOIN Teams T1 ON pass_from = T1.player_id
    INNER JOIN Teams T2 ON pass_to = T2.player_id
GROUP BY
    T1.team_name,
    case when time_stamp <= '45:00' then 1 else 2 end
ORDER BY
    team_name,
    half_number;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (team_name, half_number, score) as (
    select t1.team_name as team_name,
           case when p.time_stamp <= '45:00' then 1 else 2 end as half_number,
           case when t1.team_name = t2.team_name then 1 else -1 end as score
      from passes p
           inner join teams t1 on (t1.player_id = p.pass_from)
           inner join teams t2 on (t2.player_id = p.pass_to)
)
select team_name, half_number, sum(score) as dominance
  from t
 group by team_name, half_number
 order by team_name, half_number
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (team_name, half_number, score) as (
    select t1.team_name as team_name,
           case when p.time_stamp <= '45:00' then 1 else 2 end as half_number,
           case when t1.team_name = t2.team_name then 1 else -1 end as score
      from passes p
           inner join teams t1 on (t1.player_id = p.pass_from)
           inner join teams t2 on (t2.player_id = p.pass_to)
)
select team_name, half_number, sum(score) as dominance
  from t
 group by team_name, half_number
 order by team_name, half_number
;


# MySQL
# Write your MySQL query statement below
with t (team_name, half_number, score) as (
    select t1.team_name as team_name,
           case when p.time_stamp <= '45:00' then 1 else 2 end as half_number,
           case when t1.team_name = t2.team_name then 1 else -1 end as score
      from passes p
           inner join teams t1 on (t1.player_id = p.pass_from)
           inner join teams t2 on (t2.player_id = p.pass_to)
)
select team_name, half_number, sum(score) as dominance
  from t
 group by team_name, half_number
 order by team_name, half_number
;


# Pandas
import pandas as pd

def calculate_team_dominance(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    df = ( passes
          .merge(teams, how='inner', left_on='pass_from', right_on='player_id')
          .merge(teams, how='inner', left_on='pass_to', right_on='player_id')
         )
    df = df.assign(dominance=np.where(df['team_name_x'] == df['team_name_y'], 1, -1),
                   half_number=np.where(df['time_stamp'] <= '45:00', 1, 2)
                  )
    return ( df
            .groupby(by=['team_name_x', 'half_number'], as_index=0)['dominance']
            .sum()
            .rename(columns={'team_name_x': 'team_name'})
            .sort_values(by=['team_name', 'half_number'])
           )

