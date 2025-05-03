-- Oracle
/* Write your PL/SQL query statement below */
select problem_id
from problems
where likes / (likes + dislikes) < 0.6
order by 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select problem_id
from problems
where likes::float / (likes + dislikes)::float < 0.6
order by 1
;


-- SQL Server
/* Write your T-SQL query statement below */
select problem_id
from problems
where convert(float, likes) / convert(float, (likes + dislikes)) < 0.6
order by 1
;


# MySQL
# Write your MySQL query statement below
select problem_id
from problems
where likes / (likes + dislikes) < 0.6
order by 1
;


# Pandas
import pandas as pd

def low_quality_problems(problems: pd.DataFrame) -> pd.DataFrame:
    problems['quality'] = problems['likes']/(problems['likes'] + problems['dislikes'])
    return problems[problems['quality'] < 0.6][['problem_id']].sort_values('problem_id')

