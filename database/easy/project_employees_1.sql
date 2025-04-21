-- Oracle
/* Write your PL/SQL query statement below */
select p.project_id, round(sum(e.experience_years)/count(e.employee_id), 2) as average_years
from project p
     inner join employee e on (e.employee_id = p.employee_id)
group by p.project_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select p.project_id,
       round(avg(e.experience_years), 2) as average_years
  from project p
       inner join employee e on (e.employee_id = p.employee_id)
 group by p.project_id
;


-- SQL Server
/* Write your T-SQL query statement below */
-- Do not convert to float. Convert to decimal instead.
-- In case of float, round(15.475) = 15.47 and for decimal, it is 15.48.
select p.project_id,
       round(avg(convert(decimal, e.experience_years)), 2) as average_years
  from project p
       inner join employee e on (e.employee_id = p.employee_id)
 group by p.project_id
 order by p.project_id
;


# MySQL
# Write your MySQL query statement below
select p.project_id,
       round(avg(e.experience_years), 2) as average_years
  from project p
       inner join employee e on (e.employee_id = p.employee_id)
 group by p.project_id
;


# Pandas
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = ( project
          .merge(employee, how='inner', on='employee_id')
          .groupby('project_id', as_index=0)
          .agg(average_years=('experience_years', 'mean'))
         )
    df['average_years'] = round(df['average_years'], 2)
    return df

