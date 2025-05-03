-- Oracle
/* Write your PL/SQL query statement below */
update salary
   set sex = case sex when 'f' then 'm' else 'f' end
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
update salary
   set sex = case sex when 'f' then 'm' else 'f' end
;


-- SQL Server
/* Write your T-SQL query statement below */
update salary
   set sex = case sex when 'f' then 'm' else 'f' end
;


# MySQL
# Write your MySQL query statement below
update salary
   set sex = case sex when 'f' then 'm' else 'f' end
;


# Pandas
import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = np.where(salary['sex'] == 'm', 'f', 'm')
    return salary

