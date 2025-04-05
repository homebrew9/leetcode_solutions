-- Oracle
/* Write your PL/SQL query statement below */
with t (employee_id, name, salary, same_salary_count) as (
select employee_id, name, salary,
       count(*) over (partition by salary) as same_salary_count
from employees
),
t1 (employee_id, name, salary, same_salary_count, team_id) as (
select employee_id, name, salary, same_salary_count,
       dense_rank() over (order by salary) as team_id
from t
where same_salary_count > 1
)
select employee_id, name, salary, team_id
from t1
order by team_id, employee_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (employee_id, name, salary, same_salary_count) as (
select employee_id, name, salary,
       count(*) over (partition by salary) as same_salary_count
from employees
),
t1 (employee_id, name, salary, same_salary_count, team_id) as (
select employee_id, name, salary, same_salary_count,
       dense_rank() over (order by salary) as team_id
from t
where same_salary_count > 1
)
select employee_id, name, salary, team_id
from t1
order by team_id, employee_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (employee_id, name, salary, same_salary_count) as (
select employee_id, name, salary,
       count(*) over (partition by salary) as same_salary_count
from employees
),
t1 (employee_id, name, salary, same_salary_count, team_id) as (
select employee_id, name, salary, same_salary_count,
       dense_rank() over (order by salary) as team_id
from t
where same_salary_count > 1
)
select employee_id, name, salary, team_id
from t1
order by team_id, employee_id
;


# MySQL
# Write your MySQL query statement below
with t (employee_id, name, salary, same_salary_count) as (
select employee_id, name, salary,
       count(*) over (partition by salary) as same_salary_count
from employees
),
t1 (employee_id, name, salary, same_salary_count, team_id) as (
select employee_id, name, salary, same_salary_count,
       dense_rank() over (order by salary) as team_id
from t
where same_salary_count > 1
)
select employee_id, name, salary, team_id
from t1
order by team_id, employee_id
;


# Pandas
import pandas as pd

def employees_of_same_salary(employees: pd.DataFrame) -> pd.DataFrame:
    repeated_salary = ( employees
                       .groupby('salary', as_index=False)['employee_id']
                       .count()
                       .query('employee_id > 1')['salary']
                      )
    df = employees[employees['salary'].isin(repeated_salary)]
    # I encounter a the following warning if I do not create a copy!
    # =================================
    # "SettingWithCopyWarning:
    #  A value is trying to be set on a copy of a slice from a DataFrame.
    #  Try using .loc[row_indexer,col_indexer] = value instead"
    # =================================
    df1 = df.copy(deep=False)
    df1['team_id'] = df1['salary'].rank(method='dense').astype(int)
    return df1.sort_values(['team_id','employee_id'])

