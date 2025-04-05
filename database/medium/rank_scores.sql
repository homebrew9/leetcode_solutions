-- Oracle
/* Write your PL/SQL query statement below */
select score, dense_rank() over (order by score desc) as rank
from scores
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select score, dense_rank() over (order by score desc) as rank
from scores
;


-- SQL Server
/* Write your T-SQL query statement below */
select score, dense_rank() over (order by score desc) as rank
from scores
;


# MySQL
# Write your MySQL query statement below
select score, dense_rank() over (order by score desc) as "rank"
from scores
;


# Pandas
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    return (  scores.assign(
                  rank=scores['score']
                       .rank(method='dense',ascending=False)
                       .astype('int')
              )[['score','rank']]
              .sort_values(by='rank')
           )

