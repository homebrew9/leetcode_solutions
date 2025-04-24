-- Oracle
/* Write your PL/SQL query statement below */
select actor_id, director_id
  from ActorDirector
 group by actor_id, director_id
having count(*) >= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select actor_id, director_id
  from ActorDirector
 group by actor_id, director_id
having count(*) >= 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select actor_id, director_id, count(*) as cnt
from ActorDirector
group by actor_id, director_id
having count(*) >= 3
)
select actor_id, director_id from t
;

# MySQL
# Write your MySQL query statement below
select actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) >= 3
;


# Pandas
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return actor_director.groupby(
               by=['actor_id','director_id'], as_index=False
           ).agg(
               cooperated=('actor_id','count')
           ).query(
               'cooperated >= 3'
           )[['actor_id','director_id']]

