-- Oracle
/* Write your PL/SQL query statement below */
select x.project_id, y.employee_id
  from project x
       inner join employee y on (y.employee_id = x.employee_id)
 where (x.project_id, y.experience_years) IN (select p.project_id, max(e.experience_years)
                                                from project p
                                                     inner join employee e on (e.employee_id = p.employee_id)
                                               group by p.project_id
                                             )
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (project_id, employee_id, experience_years, max_exp) as (
select p.project_id, e.employee_id, e.experience_years,
       max(e.experience_years) over (partition by p.project_id) as max_exp
from project p
     inner join employee e on (e.employee_id = p.employee_id)
)
select project_id, employee_id
from t
where experience_years = max_exp
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (project_id, employee_id, experience_years, max_exp) as (
select p.project_id, e.employee_id, e.experience_years,
       max(e.experience_years) over (partition by p.project_id) as max_exp
from project p
     inner join employee e on (e.employee_id = p.employee_id)
)
select project_id, employee_id
from t
where experience_years = max_exp
;


# MySQL
# Write your MySQL query statement below
with t (project_id, employee_id, experience_years, max_exp) as (
select p.project_id, e.employee_id, e.experience_years,
       max(e.experience_years) over (partition by p.project_id) as max_exp
from project p
     inner join employee e on (e.employee_id = p.employee_id)
)
select project_id, employee_id
from t
where experience_years = max_exp
;


# Pandas
import pandas as pd

def project_employees(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    project_max_exp = ( project
                       .merge(employee, how='inner', on='employee_id')
                       .groupby('project_id',as_index=False)['experience_years']
                       .max()
                      )
    project_emp = ( project
                   .merge(employee, how='inner', on='employee_id')[['project_id','employee_id','experience_years']]
                  )
    return ( project_emp
            .merge(project_max_exp, how='inner', on=['project_id','experience_years'])[['project_id','employee_id']]
           )

