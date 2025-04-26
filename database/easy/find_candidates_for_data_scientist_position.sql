-- Oracle
/* Write your PL/SQL query statement below */
select x.candidate_id from (
select candidate_id from candidates where skill = 'Python'
intersect
select candidate_id from candidates where skill = 'Tableau'
intersect
select candidate_id from candidates where skill = 'PostgreSQL'
) x
order by x.candidate_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select x.candidate_id from (
select candidate_id from candidates where skill = 'Python'
intersect
select candidate_id from candidates where skill = 'Tableau'
intersect
select candidate_id from candidates where skill = 'PostgreSQL'
) x
order by x.candidate_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select x.candidate_id from (
select candidate_id from candidates where skill = 'Python'
intersect
select candidate_id from candidates where skill = 'Tableau'
intersect
select candidate_id from candidates where skill = 'PostgreSQL'
) x
order by x.candidate_id
;


# MySQL
# Write your MySQL query statement below
select x.candidate_id from (
select candidate_id from candidates where skill = 'Python'
intersect
select candidate_id from candidates where skill = 'Tableau'
intersect
select candidate_id from candidates where skill = 'PostgreSQL'
) x
order by x.candidate_id
;


# Pandas
import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    return ( candidates[candidates['skill']=='Python']
            .merge(candidates[candidates['skill']=='Tableau'], how='inner', on='candidate_id')
            .merge(candidates[candidates['skill']=='PostgreSQL'], how='inner', on='candidate_id')[['candidate_id']]
            .sort_values('candidate_id')
           )

