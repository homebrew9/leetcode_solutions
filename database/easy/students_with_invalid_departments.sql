-- Oracle
/* Write your PL/SQL query statement below */
select s.id, s.name
  from students s
 where not exists (select null
                     from departments d
                    where d.id = s.department_id
                  )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select s.id, s.name
from students s
where s.department_id not in (select d.id from departments d)
;


-- SQL Server
/* Write your T-SQL query statement below */
select s.id, s.name
from students s
where s.department_id not in (select d.id from departments d)
;


# MySQL
# Write your MySQL query statement below
select s.id, s.name
from students s
where s.department_id not in (select d.id from departments d)
;


# Pandas
import pandas as pd

def find_students(departments: pd.DataFrame, students: pd.DataFrame) -> pd.DataFrame:
    existing_departments = departments['id']
    return students[~students['department_id'].isin(existing_departments)][['id','name']]

