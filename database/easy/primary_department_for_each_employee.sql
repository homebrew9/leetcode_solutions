-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (employee_id, department_id, primary_flag, dept_count) as (
    select employee_id, department_id, primary_flag,
           count(*) over (partition by employee_id) as dept_count
      from employee
)
select employee_id, department_id
  from t
 where dept_count = 1
    or primary_flag = 'Y'
;


-- SQL Server


# MySQL


# Pandas
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    return ( employee
        .merge( employee.groupby('employee_id', as_index=0).agg(dept_count=('department_id', 'count')),
                how='inner',
                on='employee_id'
              )
        .query("dept_count==1 or primary_flag=='Y'")[['employee_id','department_id']]
       )

