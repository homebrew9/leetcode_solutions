-- Oracle
/* Write your PL/SQL query statement below */
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


-- SQL Server
/* Write your T-SQL query statement below */
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


# MySQL
# Write your MySQL query statement below
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


# Pandas
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby('managerId', as_index=False).agg(reporting=('id','count')).query('reporting >= 5')['managerId']
    return employee[employee['id'].isin(df)][['name']]

