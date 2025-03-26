-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select th.team_id as host_team_id, th.team_name as host_team_name,
           tg.team_id as guest_team_id, tg.team_name as guest_team_name,
           case when m.host_goals > m.guest_goals then 3
                when m.host_goals = m.guest_goals then 1
                else 0
           end as host_points,
           case when m.guest_goals > m.host_goals then 3
                when m.guest_goals = m.host_goals then 1
                else 0
           end as guest_points
      from matches m
           inner join teams th on (th.team_id = m.host_team)
           inner join teams tg on (tg.team_id = m.guest_team)
),
t1 (team_id, team_name, team_points) as (
    select host_team_id, host_team_name, host_points
      from t
    union all
    select guest_team_id, guest_team_name, guest_points
      from t
    union all
    select tm.team_id, tm.team_name, 0
      from teams tm
     where not exists (select null from t where t.host_team_id = tm.team_id)
       and not exists (select null from t where t.guest_team_id = tm.team_id)
)
select team_id, team_name, sum(team_points) as num_points
  from t1
 group by team_id, team_name
 order by num_points desc, team_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with x (team_id, points) as (
select host_team as team_id,
       sum(case when host_goals > guest_goals then 3 when host_goals = guest_goals then 1 else 0 end) as points
  from matches
 group by host_team
union all
select guest_team as team_id,
       sum(case when guest_goals > host_goals then 3 when guest_goals = host_goals then 1 else 0 end) as points
  from matches
 group by guest_team
)
select t.team_id, t.team_name, coalesce(sum(x.points), 0) as num_points
from teams t
     left outer join x on (x.team_id = t.team_id)
group by t.team_id, t.team_name
order by num_points desc, t.team_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with x (team_id, points) as (
select host_team as team_id,
       sum(case when host_goals > guest_goals then 3 when host_goals = guest_goals then 1 else 0 end) as points
  from matches
 group by host_team
union all
select guest_team as team_id,
       sum(case when guest_goals > host_goals then 3 when guest_goals = host_goals then 1 else 0 end) as points
  from matches
 group by guest_team
)
select t.team_id, t.team_name, coalesce(sum(x.points), 0) as num_points
from teams t
     left outer join x on (x.team_id = t.team_id)
group by t.team_id, t.team_name
order by num_points desc, t.team_id
;


# MySQL
# Write your MySQL query statement below
with x (team_id, points) as (
select host_team as team_id,
       sum(case when host_goals > guest_goals then 3 when host_goals = guest_goals then 1 else 0 end) as points
  from matches
 group by host_team
union all
select guest_team as team_id,
       sum(case when guest_goals > host_goals then 3 when guest_goals = host_goals then 1 else 0 end) as points
  from matches
 group by guest_team
)
select t.team_id, t.team_name, coalesce(sum(x.points), 0) as num_points
from teams t
     left outer join x on (x.team_id = t.team_id)
group by t.team_id, t.team_name
order by num_points desc, t.team_id
;


# Pandas
import pandas as pd

def team_scores(teams: pd.DataFrame, matches: pd.DataFrame) -> pd.DataFrame:
    matches['host_points'] = np.where(
                               matches['host_goals'] > matches['guest_goals'], 3,
                               np.where(matches['host_goals'] == matches['guest_goals'], 1, 0)
                             )
    matches['guest_points'] = np.where(
                                matches['guest_goals'] > matches['host_goals'], 3,
                                np.where(matches['guest_goals'] == matches['host_goals'], 1, 0)
                              )
    df1 = (  matches[['host_team','host_points']]
             .rename(columns={'host_team':'team_id', 'host_points':'num_points'})
             .groupby('team_id',as_index=False)['num_points']
             .sum()
          )
    df2 = (  matches[['guest_team','guest_points']]
             .rename(columns={'guest_team':'team_id', 'guest_points':'num_points'})
             .groupby('team_id',as_index=False)['num_points']
             .sum()
          )
    df = pd.concat([df1, df2]).groupby('team_id',as_index=False)['num_points'].sum()
    return (  teams
              .merge(df, how='left', on='team_id')
              .fillna(0)
              .sort_values(by=['num_points','team_id'], ascending=[False,True])
           )

