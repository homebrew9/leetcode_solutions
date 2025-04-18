-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select u.id, u.name, coalesce(sum(r.distance), 0) as travelled_distance
      from users u
           left join rides r on (r.user_id = u.id)
     group by u.id, u.name
     order by travelled_distance desc, u.name
)
select t.name, t.travelled_distance
  from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select u.id, u.name, coalesce(sum(r.distance), 0) as travelled_distance
      from users u
           left join rides r on (r.user_id = u.id)
     group by u.id, u.name
     order by travelled_distance desc, u.name
)
select t.name, t.travelled_distance
  from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select u.id, u.name, coalesce(sum(r.distance), 0) as travelled_distance
      from users u
           left join rides r on (r.user_id = u.id)
     group by u.id, u.name
)
select t.name, t.travelled_distance
  from t
 order by t.travelled_distance desc, t.name
;


# MySQL


# Pandas
import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    return ( users
            .merge(rides, how='left', left_on='id', right_on='user_id')
            .groupby(['id_x','name'],as_index=0)['distance']
            .sum()
            .sort_values(by=['distance','name'], ascending=[False,True])[['name','distance']]
            .rename(columns={'distance': 'travelled_distance'})
           )

