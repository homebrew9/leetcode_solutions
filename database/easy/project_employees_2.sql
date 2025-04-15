-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
with t (project_id, employee_count) as (
    select project_id, count(employee_id)
      from project
     group by project_id
),
t1 (project_id, employee_count, max_employee_count) as (
    select project_id, employee_count,
           max(employee_count) over () as max_employee_count
      from t
)
select project_id as "project_id"
from t1
where employee_count = max_employee_count
;


# MySQL
# Write your MySQL query statement below
with t (project_id, employee_count) as (
    select project_id, count(employee_id)
      from project
     group by project_id
),
t1 (project_id, employee_count, max_employee_count) as (
    select project_id, employee_count,
           max(employee_count) over () as max_employee_count
      from t
)
select project_id as "project_id"
from t1
where employee_count = max_employee_count
;


# Pandas
import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.groupby('project_id', as_index=False)['employee_id'].count()
    return df[df['employee_id'] == df['employee_id'].max()][['project_id']]

