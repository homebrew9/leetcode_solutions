-- Oracle
/* Write your PL/SQL query statement below */
select max(assignment1 + assignment2 + assignment3) - min(assignment1 + assignment2 + assignment3) as difference_in_score
from scores
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select max(assignment1 + assignment2 + assignment3) - min(assignment1 + assignment2 + assignment3) as difference_in_score
  from scores
;


-- SQL Server
/* Write your T-SQL query statement below */
select max(assignment1 + assignment2 + assignment3) - min(assignment1 + assignment2 + assignment3) as difference_in_score
from scores
;


# MySQL
# Write your MySQL query statement below
select max(assignment1 + assignment2 + assignment3) - min(assignment1 + assignment2 + assignment3) as difference_in_score
from scores
;


# Pandas
import pandas as pd

def class_performance(scores: pd.DataFrame) -> pd.DataFrame:
    scores['total_score'] = scores['assignment1'] + scores['assignment2'] + scores['assignment3']
    diff = scores['total_score'].max() - scores['total_score'].min()
    return pd.DataFrame(data={'difference_in_score': [diff]})

