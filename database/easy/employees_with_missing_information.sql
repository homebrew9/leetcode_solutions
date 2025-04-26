-- Oracle
/* Write your PL/SQL query statement below */
select coalesce(e.employee_id, s.employee_id) as employee_id
  from employees e
       full outer join salaries s on (e.employee_id = s.employee_id)
where (e.employee_id is null or s.employee_id is null)
order by employee_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select coalesce(e.employee_id, s.employee_id) as employee_id
  from employees e
       full outer join salaries s on (e.employee_id = s.employee_id)
where (e.employee_id is null or s.employee_id is null)
order by employee_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select coalesce(e.employee_id, s.employee_id) as employee_id
  from employees e
       full outer join salaries s on (e.employee_id = s.employee_id)
where (e.employee_id is null or s.employee_id is null)
order by employee_id
;


# MySQL
# Write your MySQL query statement below
select employee_id from employees where employee_id not in (select employee_id from salaries)
union
select employee_id from salaries where employee_id not in (select employee_id from employees)
order by 1
;


# Pandas
import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    missing_salary = employees[~employees['employee_id'].isin(salaries['employee_id'])][['employee_id']]
    missing_name = salaries[~salaries['employee_id'].isin(employees['employee_id'])][['employee_id']]
    return pd.concat([missing_name, missing_salary]).sort_values('employee_id')

