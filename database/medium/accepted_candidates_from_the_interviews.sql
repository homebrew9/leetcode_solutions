-- Oracle
/* Write your PL/SQL query statement below */
select c.candidate_id
from candidates c
     inner join rounds r on (r.interview_id = c.interview_id)
where c.years_of_exp >= 2
group by c.candidate_id
having sum(r.score) > 15
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select c.candidate_id
from candidates c
     inner join rounds r on (r.interview_id = c.interview_id)
where c.years_of_exp >= 2
group by c.candidate_id
having sum(r.score) > 15
;


-- SQL Server
/* Write your T-SQL query statement below */
select c.candidate_id
from candidates c
     inner join rounds r on (r.interview_id = c.interview_id)
where c.years_of_exp >= 2
group by c.candidate_id
having sum(r.score) > 15
;


# MySQL
# Write your MySQL query statement below
select c.candidate_id
from candidates c
     inner join rounds r on (r.interview_id = c.interview_id)
where c.years_of_exp >= 2
group by c.candidate_id
having sum(r.score) > 15
;


# Pandas
import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    return (  candidates[candidates['years_of_exp'] >= 2]
              .merge(rounds, how='inner', on='interview_id')
              .groupby('candidate_id',as_index=False)['score']
              .sum()
              .query('score > 15')[['candidate_id']]
           )

