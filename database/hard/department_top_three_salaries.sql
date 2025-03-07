-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select d.name as department,
       e.name as employee,
       e.salary,
       dense_rank() over (partition by d.id order by e.salary desc) as drnk
from employee e
     inner join department d on (d.id = e.departmentId)
)
select department, employee, salary
from t
where drnk <= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select d.name as department,
       e.name as employee,
       e.salary,
       dense_rank() over (partition by d.id order by e.salary desc) as drnk
from employee e
     inner join department d on (d.id = e.departmentId)
)
select department, employee, salary
from t
where drnk <= 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select d.name as department,
       e.name as employee,
       e.salary,
       dense_rank() over (partition by d.id order by e.salary desc) as drnk
from employee e
     inner join department d on (d.id = e.departmentId)
)
select department, employee, salary
from t
where drnk <= 3
;


# MySQL
# Write your MySQL query statement below
with t as (
select d.name as department,
       e.name as employee,
       e.salary,
       dense_rank() over (partition by d.id order by e.salary desc) as drnk
from employee e
     inner join department d on (d.id = e.departmentId)
)
select department, employee, salary
from t
where drnk <= 3
;


# Pandas
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = department.merge(employee, how='inner', left_on='id', right_on='departmentId')
    return ( df
            .assign(
                      rnk =  df
                            .groupby('departmentId', as_index=False)['salary']
                            .rank('dense',ascending=False)
                   )
            .query('rnk <= 3')[['name_x','name_y','salary']]
            .rename(columns={'name_x':'Department', 'name_y':'Employee', 'salary': 'Salary'})
           )

