-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select t1.team_name, p.time_stamp,
           case when t1.team_name = t2.team_name then 'C' else 'I' end as pass_type
      from passes p
           inner join teams t1 on (t1.player_id = p.pass_from)
           inner join teams t2 on (t2.player_id = p.pass_to)
),
t1 as (
    select team_name, time_stamp, pass_type,
           case
               when pass_type <> coalesce(lag(pass_type) over (partition by team_name order by time_stamp), 'X')
               then 1
               else 0
           end as marker
      from t
),
t2 as (
    select team_name, time_stamp, pass_type, marker,
           sum(marker) over (order by team_name, time_stamp) as group_id
      from t1
),
t3 as (
    select team_name, group_id, count(*) as pass_streak
      from t2
     where pass_type = 'C'
     group by team_name, group_id
)
select team_name, max(pass_streak) as longest_streak
  from t3
 group by team_name
 order by team_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select t1.team_name, p.time_stamp,
           case when t1.team_name = t2.team_name then 'C' else 'I' end as pass_type
      from passes p
           inner join teams t1 on (t1.player_id = p.pass_from)
           inner join teams t2 on (t2.player_id = p.pass_to)
),
t1 as (
    select team_name, time_stamp, pass_type,
           case
               when pass_type <> coalesce(lag(pass_type) over (partition by team_name order by time_stamp), 'X')
               then 1
               else 0
           end as marker
      from t
),
t2 as (
    select team_name, time_stamp, pass_type, marker,
           sum(marker) over (order by team_name, time_stamp) as group_id
      from t1
),
t3 as (
    select team_name, group_id, count(*) as pass_streak
      from t2
     where pass_type = 'C'
     group by team_name, group_id
)
select team_name, max(pass_streak) as longest_streak
  from t3
 group by team_name
 order by team_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select t1.team_name, p.time_stamp,
           case when t1.team_name = t2.team_name then 'C' else 'I' end as pass_type
      from passes p
           inner join teams t1 on (t1.player_id = p.pass_from)
           inner join teams t2 on (t2.player_id = p.pass_to)
),
t1 as (
    select team_name, time_stamp, pass_type,
           case
               when pass_type <> coalesce(lag(pass_type) over (partition by team_name order by time_stamp), 'X')
               then 1
               else 0
           end as marker
      from t
),
t2 as (
    select team_name, time_stamp, pass_type, marker,
           sum(marker) over (order by team_name, time_stamp) as group_id
      from t1
),
t3 as (
    select team_name, group_id, count(*) as pass_streak
      from t2
     where pass_type = 'C'
     group by team_name, group_id
)
select team_name, max(pass_streak) as longest_streak
  from t3
 group by team_name
 order by team_name
;


# MySQL
# Write your MySQL query statement below
with t as (
    select t1.team_name, p.time_stamp,
           case when t1.team_name = t2.team_name then 'C' else 'I' end as pass_type
      from passes p
           inner join teams t1 on (t1.player_id = p.pass_from)
           inner join teams t2 on (t2.player_id = p.pass_to)
),
t1 as (
    select team_name, time_stamp, pass_type,
           case
               when pass_type <> coalesce(lag(pass_type) over (partition by team_name order by time_stamp), 'X')
               then 1
               else 0
           end as marker
      from t
),
t2 as (
    select team_name, time_stamp, pass_type, marker,
           sum(marker) over (order by team_name, time_stamp) as group_id
      from t1
),
t3 as (
    select team_name, group_id, count(*) as pass_streak
      from t2
     where pass_type = 'C'
     group by team_name, group_id
)
select team_name, max(pass_streak) as longest_streak
  from t3
 group by team_name
 order by team_name
;


# Pandas
import pandas as pd

def calculate_longest_streaks(teams: pd.DataFrame, passes: pd.DataFrame) -> pd.DataFrame:
    df = ( passes
          .merge(teams, how='inner', left_on='pass_from', right_on='player_id')
          .merge(teams, how='inner', left_on='pass_to', right_on='player_id')
         )
    df['pass_type'] = np.where(df.team_name_x==df.team_name_y, 'C', 'I')
    df = ( df[['team_name_x','time_stamp','pass_type']]
          .rename(columns={'team_name_x': 'team_name'})
          .sort_values(['team_name','time_stamp'])
         )
    df['marker'] = np.where(df['pass_type'].shift(1) != df['pass_type'], 1, 0)
    df['group_id'] = df['marker'].cumsum()
    return ( df[df['pass_type']=='C']
            .groupby(['team_name','group_id'], as_index=0)['pass_type']
            .count()
            .groupby('team_name', as_index=0)['pass_type']
            .max()
            .rename(columns={'pass_type': 'longest_streak'})
            .sort_values('team_name')
           )

