-- Oracle
/* Write your PL/SQL query statement below */
select employee_id,
       count(*) over (partition by team_id) as team_size
  from employee
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- Analytic function
select employee_id,
       count(employee_id) over (partition by team_id) as team_size
from employee
;


-- SQL Server
/* Write your T-SQL query statement below */
-- Subquery with group by and join
select x.employee_id,
       y.team_size
from employee x
     inner join (select e.team_id, count(*) as team_size from employee e group by e.team_id) y
     on (x.team_id = y.team_id)
;


# MySQL
# Write your MySQL query statement below
-- Subquery with group by and join
select x.employee_id,
       y.team_size
from employee x
     inner join (select e.team_id, count(*) as team_size from employee e group by e.team_id) y
     on (x.team_id = y.team_id)
;


# Pandas
import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    df = ( employee.groupby('team_id', as_index=False)['employee_id']
           .count()
           .rename(columns={'employee_id':'team_size'})
         )
    return employee.merge(df, how='inner', on='team_id')[['employee_id', 'team_size']]
    
