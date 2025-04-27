-- Oracle
/* Write your PL/SQL query statement below */
select u.user_id, u.name, coalesce(sum(r.distance), 0) as "traveled distance"
  from users u
       left outer join rides r on (r.user_id = u.user_id)
 group by u.user_id, u.name
 order by u.user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select u.user_id, u.name, coalesce(sum(r.distance), 0) as "traveled distance"
  from users u
       left outer join rides r on (r.user_id = u.user_id)
 group by u.user_id, u.name
 order by u.user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select u.user_id, u.name, coalesce(sum(r.distance), 0) as "traveled distance"
  from users u
       left outer join rides r on (r.user_id = u.user_id)
 group by u.user_id, u.name
 order by u.user_id
;


# MySQL
# Write your MySQL query statement below
select u.user_id, u.name, coalesce(sum(r.distance), 0) as "traveled distance"
  from users u
       left outer join rides r on (r.user_id = u.user_id)
 group by u.user_id, u.name
 order by u.user_id
;


# Pandas
import pandas as pd

def get_total_distance(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    return ( users
            .merge(rides, how='left', on='user_id')
            .groupby(['user_id','name'], as_index=0)['distance']
            .sum()
            .fillna(0)
            .rename(columns={'distance': 'traveled distance'})
            .sort_values(['user_id'])
           )

