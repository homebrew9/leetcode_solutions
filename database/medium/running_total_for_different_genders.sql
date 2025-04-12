-- Oracle
/* Write your PL/SQL query statement below */
select gender, to_char(day, 'yyyy-mm-dd') as day,
       sum(score_points) over (partition by gender order by day) as total
from scores
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select gender, day,
       sum(score_points) over (partition by gender order by day) as total
from scores
;


-- SQL Server
/* Write your T-SQL query statement below */
select gender, day,
       sum(score_points) over (partition by gender order by day) as total
from scores
;


# MySQL
# Write your MySQL query statement below
select gender, day,
       sum(score_points) over (partition by gender order by day) as total
from scores
;


# Pandas
import pandas as pd

def running_total(scores: pd.DataFrame) -> pd.DataFrame:
    scores['total'] = scores.sort_values(by=['gender','day']).groupby('gender')['score_points'].cumsum()
    return scores[['gender','day','total']].sort_values(by=['gender','day'])

