-- Oracle
/* Write your PL/SQL query statement below */
with t (dept_id, dept_name, student_number) as (
    select d.dept_id, d.dept_name, count(student_id) as student_number
      from department d
           left outer join student s on (s.dept_id = d.dept_id)
     group by d.dept_id, d.dept_name
)
select dept_name, student_number
  from t
 order by student_number desc, dept_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (dept_id, dept_name, student_number) as (
    select d.dept_id, d.dept_name, count(student_id) as student_number
      from department d
           left outer join student s on (s.dept_id = d.dept_id)
     group by d.dept_id, d.dept_name
)
select dept_name, student_number
  from t
 order by student_number desc, dept_name
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (dept_id, dept_name, student_number) as (
    select d.dept_id, d.dept_name, count(student_id) as student_number
      from department d
           left outer join student s on (s.dept_id = d.dept_id)
     group by d.dept_id, d.dept_name
)
select dept_name, student_number
  from t
 order by student_number desc, dept_name
;


# MySQL
# Write your MySQL query statement below
with t (dept_id, dept_name, student_number) as (
select d.dept_id, d.dept_name, count(student_id) as student_number
from department d
     left outer join student s on (s.dept_id = d.dept_id)
group by d.dept_id, d.dept_name
)
select dept_name, student_number
from t
order by student_number desc, dept_name
;


# Pandas
import pandas as pd

def count_students(student: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    return ( department
            .merge(student, how='left', on='dept_id')
            .groupby(['dept_id','dept_name'], as_index=False)['student_id']
            .count()
            .rename(columns={'student_id':'student_number'})
            .sort_values(by=['student_number','dept_name'],ascending=[False,True])[['dept_name','student_number']]
           )

