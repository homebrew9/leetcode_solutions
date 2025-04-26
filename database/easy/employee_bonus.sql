-- Oracle
/* Write your PL/SQL query statement below */
with t (e_empid, name, b_empid, bonus) as (
select e.empId as e_empid, e.name, b.empId as b_empid, b.bonus
from employee e
     left outer join bonus b on (b.empId = e.empId)
)
select name, bonus
from t
where b_empId is null or bonus < 1000
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e.name, b.bonus
  from employee e
       left outer join bonus b on (b.empId = e.empId)
 where b.bonus is null or b.bonus < 1000
;


-- SQL Server
/* Write your T-SQL query statement below */
select e.name, b.bonus
  from employee e
       left outer join bonus b on (b.empId = e.empId)
 where b.bonus is null or b.bonus < 1000
;


# MySQL
# Write your MySQL query statement below
select e.name, b.bonus
  from employee e
       left outer join bonus b on (b.empId = e.empId)
 where b.bonus is null or b.bonus < 1000
;

 
# Pandas
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    return employee.merge(bonus, how='left', on='empId').query('bonus.isnull() or bonus < 1000')[['name', 'bonus']]

