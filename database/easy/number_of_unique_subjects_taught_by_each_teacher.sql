-- Oracle
/* Write your PL/SQL query statement below */
select teacher_id, count(distinct subject_id) as cnt
  from teacher
 group by teacher_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select teacher_id, count(distinct subject_id) as cnt
  from teacher
 group by teacher_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select teacher_id, count(distinct subject_id) as cnt
  from teacher
 group by teacher_id
;


# MySQL
# Write your MySQL query statement below
select teacher_id, count(distinct subject_id) as cnt
  from teacher
 group by teacher_id
;


# Pandas
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return ( teacher[['teacher_id', 'subject_id']]
            .drop_duplicates()
            .groupby('teacher_id', as_index=0)['subject_id']
            .count()
            .rename(columns={'subject_id':'cnt'})
           )

