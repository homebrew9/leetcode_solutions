-- Oracle
/* Write your PL/SQL query statement below */
select eu.unique_id, e.name
from Employees e
     left outer join EmployeeUNI eu on (eu.id = e.id)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select eu.unique_id, e.name
  from Employees e
       left outer join EmployeeUNI eu on (eu.id = e.id)
;


-- SQL Server
/* Write your T-SQL query statement below */
select eu.unique_id, e.name
  from Employees e
       left outer join EmployeeUNI eu on (eu.id = e.id)
;


# MySQL
# Write your MySQL query statement below
select eu.unique_id, e.name
  from Employees e
       left outer join EmployeeUNI eu on (eu.id = e.id)
;


# Pandas
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employees.merge(employee_uni, how='left', on='id')[['unique_id','name']]

