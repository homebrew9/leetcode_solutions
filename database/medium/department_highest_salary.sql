-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select d.name as department, e.name as employee, e.salary,
           max(e.salary) over (partition by e.departmentId) as dept_max_salary
      from employee e
           inner join department d on (d.id = e.departmentId)
)
select department, employee, salary
  from t
 where salary = dept_max_salary
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select d.name as department, e.name as employee, e.salary,
           dense_rank() over (partition by e.departmentId order by e.salary desc) as drnk
      from employee e
           inner join department d on (d.id = e.departmentId)
)
select department, employee, salary
  from t
 where drnk = 1
;


-- SQL Server
/* Write your T-SQL query statement below */
select d.name as department, e.name as employee, e.salary
  from employee e
       inner join department d on (d.id = e.departmentId)
 where e.salary = (select max(e1.salary)
                     from employee e1
                    where e1.departmentId = e.departmentId
                  )
;


# MySQL
# Write your MySQL query statement below
select d.name as department, e.name as employee, e.salary
  from employee e
       inner join department d on (d.id = e.departmentId)
       inner join (select e1.departmentId, max(e1.salary) as salary
                     from employee e1
                    group by e1.departmentId
                  ) x
       on (x.departmentId = d.id and x.salary = e.salary)
;


# Pandas
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = ( employee
          .merge(department, how='inner', left_on='departmentId', right_on='id')
          .groupby(['id_y','name_y'], as_index=0)['salary']
          .max()
          .rename(columns={'id_y':'departmentId', 'name_y':'department'})
         )
    return ( employee
            .merge(df, how='inner', on=['departmentId','salary'])[['department','name','salary']]
            .rename(columns={'name':'employee'})
           )

