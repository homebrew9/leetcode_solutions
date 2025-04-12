-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select dept, emp_id, salary,
           dense_rank() over (partition by dept order by salary desc) as drnk
      from employees
)
select emp_id, dept
  from t
 where drnk = 2
 order by emp_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select dept, emp_id, salary,
           dense_rank() over (partition by dept order by salary desc) as drnk
      from employees
)
select emp_id, dept
  from t
 where drnk = 2
 order by emp_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select dept, emp_id, salary,
           dense_rank() over (partition by dept order by salary desc) as drnk
      from employees
)
select emp_id, dept
  from t
 where drnk = 2
 order by emp_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select dept, emp_id, salary,
           dense_rank() over (partition by dept order by salary desc) as drnk
      from employees
)
select emp_id, dept
  from t
 where drnk = 2
 order by emp_id
;


# Pandas
import pandas as pd

def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    return ( employees
            .assign(drnk=employees
                    .groupby(by='dept',as_index=0)['salary']
                    .rank(method='dense',ascending=False)
                   )
            .query('drnk==2')[['emp_id','dept']]
            .sort_values('emp_id')
           )

