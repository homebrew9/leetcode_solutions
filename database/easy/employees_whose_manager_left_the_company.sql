-- Oracle
/* Write your PL/SQL query statement below */
select x.employee_id
from employees x
where x.salary < 30000
and x.manager_id is not null
and not exists (select null from Employees y where y.employee_id = x.manager_id)
order by x.employee_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e1.employee_id
  from employees e1
 where e1.salary < 30000
   and e1.manager_id is not null
   and not exists (select null from employees e2 where e2.employee_id = e1.manager_id)
 order by e1.employee_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select e1.employee_id
  from employees e1
 where e1.salary < 30000
   and e1.manager_id is not null
   and not exists (select null from employees e2 where e2.employee_id = e1.manager_id)
 order by e1.employee_id
;


# MySQL
# Write your MySQL query statement below
select e1.employee_id
  from employees e1
 where e1.salary < 30000
   and e1.manager_id is not null
   and not exists (select null from employees e2 where e2.employee_id = e1.manager_id)
 order by e1.employee_id
;


# Pandas
import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    return ( employees[ (employees['salary'] < 30000) &
                        (~employees['manager_id'].isna()) &
                        (~employees['manager_id'].isin(employees['employee_id']))
                      ][['employee_id']]
            .sort_values('employee_id')
           )

