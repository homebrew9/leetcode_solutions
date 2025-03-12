-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select e.employee_id, p.project_id,
           e.name as employee_name,
           p.workload as project_workload,
           avg(p.workload) over (partition by e.team) as avg_workload
      from employees e
           inner join project p on (p.employee_id = e.employee_id)
)
select employee_id, project_id, employee_name, project_workload
  from t
 where project_workload > avg_workload
 order by employee_id, project_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select e.employee_id, p.project_id,
           e.name as employee_name,
           p.workload as project_workload,
           avg(p.workload) over (partition by e.team) as avg_workload
      from employees e
           inner join project p on (p.employee_id = e.employee_id)
)
select employee_id, project_id, employee_name, project_workload
  from t
 where project_workload > avg_workload
 order by employee_id, project_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select e.employee_id, p.project_id,
           e.name as employee_name,
           p.workload as project_workload,
           avg(p.workload) over (partition by e.team) as avg_workload
      from employees e
           inner join project p on (p.employee_id = e.employee_id)
)
select employee_id, project_id, employee_name, project_workload
  from t
 where project_workload > avg_workload
 order by employee_id, project_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select e.employee_id, p.project_id,
           e.name as employee_name,
           p.workload as project_workload,
           avg(p.workload) over (partition by e.team) as avg_workload
      from employees e
           inner join project p on (p.employee_id = e.employee_id)
)
select employee_id, project_id, employee_name, project_workload
  from t
 where project_workload > avg_workload
 order by employee_id, project_id
;


# Pandas
import pandas as pd

def employees_with_above_avg_workload(project: pd.DataFrame, employees: pd.DataFrame) -> pd.DataFrame:
    df = ( employees
          .merge(project, how='inner', on='employee_id')
          .rename(columns={'name': 'employee_name', 'workload': 'project_workload'})
         )
    df_avg = ( df
              .groupby('team', as_index=0)['project_workload']
              .mean()
              .rename(columns={'project_workload': 'avg_workload'})
             )
    return ( df
            .merge(df_avg, how='inner', on='team')
            .query('project_workload > avg_workload')[['employee_id','project_id','employee_name','project_workload']]
            .sort_values(['employee_id','project_id'])
           )

