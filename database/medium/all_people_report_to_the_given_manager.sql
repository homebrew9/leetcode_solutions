-- Oracle
/* Write your PL/SQL query statement below */
with t (employee_id, manager_id, depth, root, path) as (
    select employee_id, manager_id, 1, employee_id, to_char(employee_id)
      from employees
     where employee_id = manager_id
    union all
    select e.employee_id, e.manager_id, t.depth + 1, t.root, t.path || '/' || e.employee_id
      from employees e
           inner join t on (e.manager_id = t.employee_id)
     where e.employee_id != e.manager_id
)
select employee_id
  from t
 where root = 1
   and depth > 1
order by root, depth
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (employee_id) as (
    select e.employee_id
      from employees e
     where e.employee_id = 1
    union all
    select x.employee_id
      from employees x
           inner join t on (x.manager_id = t.employee_id)
     where x.employee_id != 1
)
select employee_id
from t
where employee_id != 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (employee_id) as (
    select e.employee_id
      from employees e
     where e.employee_id = 1
    union all
    select x.employee_id
      from employees x
           inner join t on (x.manager_id = t.employee_id)
     where x.employee_id != 1
)
select employee_id
from t
where employee_id != 1
;


# MySQL
# Write your MySQL query statement below
with recursive t (employee_id) as (
    select e.employee_id
      from employees e
     where e.employee_id = 1
    union all
    select x.employee_id
      from employees x
           inner join t on (x.manager_id = t.employee_id)
     where x.employee_id != 1
)
select employee_id
from t
where employee_id != 1
;


# Pandas
import pandas as pd

def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:
    res = pd.DataFrame(data={'employee_id': []})
    # Boss
    df = pd.Series([1])
    df = employees[(employees['manager_id'].isin(df)) & (employees['employee_id'] != 1)]['employee_id']
    while len(df) != 0:
        res = pd.concat([res, df.to_frame()])
        df = employees[(employees['manager_id'].isin(df)) & (employees['employee_id'] != 1)]['employee_id']
    return res

