-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
      from dual
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


# Pandas
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rnk'] = employee['salary'].drop_duplicates().rank(method='first',ascending=False)
    df = employee[employee['rnk']==2][['salary']].rename(columns={'salary': 'SecondHighestSalary'})
    return pd.DataFrame(data={'SecondHighestSalary': None}, index=[0]) if len(df) == 0 else df

