-- Oracle
/* Write your PL/SQL query statement below */
select abs(e.max_salary - m.max_salary) as salary_difference
from (select max(salary) as max_salary from salaries where department = 'Engineering') e
     cross join
     (select max(salary) as max_salary from salaries where department = 'Marketing') m
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select abs(e.max_salary - m.max_salary) as salary_difference
from (select max(salary) as max_salary from salaries where department = 'Engineering') e
     cross join
     (select max(salary) as max_salary from salaries where department = 'Marketing') m
;


-- SQL Server
/* Write your T-SQL query statement below */
select abs(e.max_salary - m.max_salary) as salary_difference
from (select max(salary) as max_salary from salaries where department = 'Engineering') e
     cross join
     (select max(salary) as max_salary from salaries where department = 'Marketing') m
;


# MySQL
# Write your MySQL query statement below
select abs(e.max_salary - m.max_salary) as salary_difference
from (select max(salary) as max_salary from salaries where department = 'Engineering') e
     cross join
     (select max(salary) as max_salary from salaries where department = 'Marketing') m
;


# Pandas
import pandas as pd

def salaries_difference(salaries: pd.DataFrame) -> pd.DataFrame:
    eng_max_salary = ( salaries[salaries['department']=='Engineering']
                       .groupby('department', as_index=False)['salary']
                       .max()['salary']
                       .item()
                     )
    mkt_max_salary = ( salaries[salaries['department']=='Marketing']
                       .groupby('department', as_index=False)['salary']
                       .max()['salary']
                       .item()
                     )
    val = abs(eng_max_salary - mkt_max_salary)
    return pd.DataFrame(data=[val], columns=['salary_difference'])

