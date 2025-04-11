-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select year, tournament, player_id
      from championships
      unpivot (
          player_id
          for tournament in (
              Wimbledon as 'Wimbledon',
              Fr_open as 'Fr_open',
              US_open as 'US_open',
              Au_open as 'Au_open'
          )
      )
)
select p.player_id, p.player_name, count(*) as grand_slams_count
  from players p
       inner join t on (t.player_id = p.player_id)
 group by p.player_id, p.player_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (player_id, titles) as (
    select wimbledon, count(*) from championships group by wimbledon
    union all
    select fr_open, count(*) from championships group by fr_open
    union all
    select us_open, count(*) from championships group by us_open
    union all
    select au_open, count(*) from championships group by au_open
)
select t.player_id, p.player_name, sum(t.titles) as grand_slams_count
from t inner join players p on (p.player_id = t.player_id)
group by t.player_id, p.player_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (year, id) as (
    select year, wimbledon from championships union all
    select year, fr_open from championships union all
    select year, us_open from championships union all
    select year, au_open from championships
)
select p.player_id, p.player_name, count(*) as grand_slams_count
from players p
     inner join t on (t.id = p.player_id)
group by p.player_id, p.player_name
;


# MySQL
# Write your MySQL query statement below
with t (player_id, titles) as (
    select wimbledon, count(*) from championships group by wimbledon
    union all
    select fr_open, count(*) from championships group by fr_open
    union all
    select us_open, count(*) from championships group by us_open
    union all
    select au_open, count(*) from championships group by au_open
)
select t.player_id, p.player_name, sum(t.titles) as grand_slams_count
from t inner join players p on (p.player_id = t.player_id)
group by t.player_id, p.player_name
;


# Pandas
import pandas as pd

def grand_slam_titles(players: pd.DataFrame, championships: pd.DataFrame) -> pd.DataFrame:
    df = (pd.concat([
                       championships[['year','Wimbledon']].rename(columns={'Wimbledon':'player_id'}),
                       championships[['year','Fr_open']].rename(columns={'Fr_open':'player_id'}),
                       championships[['year','US_open']].rename(columns={'US_open':'player_id'}),
                       championships[['year','Au_open']].rename(columns={'Au_open':'player_id'})
                    ],
                    axis=0
                   )
         )
    return ( players
            .merge(df, how='inner', on='player_id')
            .groupby(['player_id','player_name'], as_index=0)['year']
            .count()
            .rename(columns={'year': 'grand_slams_count'})
           )

