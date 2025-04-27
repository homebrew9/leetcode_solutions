-- Oracle
/* Write your PL/SQL query statement below */
with t (x) as (
    select x
      from point
     order by x
),
t1 (curr_val, next_val) as (
    select x, lead(x) over (order by x)
      from t
)
select min(next_val - curr_val) as shortest
  from t1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (x, lg, diff) as (
    select x, lag(x) over (order by x) as lg, abs(x - lag(x) over (order by x)) as diff
      from point
)
select min(diff) as "shortest" from t
;


-- SQL Server
/* Write your T-SQL query statement below */
select min(p2.x - p1.x) as shortest
from point p1
     inner join point p2 on (p2.x > p1.x)
;


# MySQL
# Write your MySQL query statement below
with t (x) as (
    select x
      from point
     order by x
),
t1 (curr_val, next_val) as (
    select x, lead(x) over (order by x)
      from t
)
select min(next_val - curr_val) as shortest
  from t1
;


# Pandas
import pandas as pd

def shortest_distance(point: pd.DataFrame) -> pd.DataFrame:
    point = point.sort_values(by=['x'])
    point['lag'] = point.shift(1)
    point = point[~point['lag'].isna()]
    point['diff'] = abs(point['x']-point['lag'])
    return pd.DataFrame(data=[min(point['diff'])], columns=['shortest'])

