-- Oracle
/* Write your PL/SQL query statement below */
with t (name, vote_count) as (
select c.name, count(*) as vote_count
from candidate c
     inner join vote v on (v.candidateId = c.id)
group by c.name
)
select name
from t
where vote_count = (select max(vote_count) from t)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (name, vote_count) as (
select c.name, count(*) as vote_count
from candidate c
     inner join vote v on (v.candidateId = c.id)
group by c.name
)
select name
from t
where vote_count = (select max(vote_count) from t)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (name, vote_count) as (
select c.name, count(*) as vote_count
from candidate c
     inner join vote v on (v.candidateId = c.id)
group by c.name
)
select name
from t
where vote_count = (select max(vote_count) from t)
;


# MySQL
# Write your MySQL query statement below
with t (name, vote_count) as (
select c.name, count(*) as vote_count
from candidate c
     inner join vote v on (v.candidateId = c.id)
group by c.name
)
select name
from t
where vote_count = (select max(vote_count) from t)
;


# Pandas
import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    df = ( candidate
          .merge(vote, how='inner', left_on='id', right_on='candidateId')
          .groupby('name',as_index=False)['id_y']
          .count()
         )
    max_vote_count = max(df['id_y'])
    return df[df['id_y']==max_vote_count][['name']]

