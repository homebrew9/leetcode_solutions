-- Oracle
/* Write your PL/SQL query statement below */
select e.name as "Employee"
  from employee e
       inner join employee m
       on (e.managerid = m.id and e.salary > m.salary)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e.name as Employee
  from employee e
       inner join employee m on (m.id = e.managerId)
 where e.salary > m.salary
;


-- SQL Server
/* Write your T-SQL query statement below */
SELECT e.name AS Employee
FROM Employee e
     INNER JOIN Employee m ON (m.id = e.managerId)
WHERE e.salary > m.salary
;


# MySQL
# Write your MySQL query statement below
select e.name as Employee
  from employee e
       inner join employee m on (m.id = e.managerId)
 where e.salary > m.salary
;


# Pandas
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    return ( employee
            .merge(employee, how='inner', left_on='managerId', right_on='id')
            .query('salary_x > salary_y')[['name_x']]
            .rename(columns={'name_x': 'Employee'})
           )

