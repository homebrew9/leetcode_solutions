-- Oracle
/* Write your PL/SQL query statement below */
select s.emp_id, s.firstname, s.lastname, s.salary, s.department_id
  from salary s
 where s.salary = (select max(t.salary)
                     from salary t
                    where t.emp_id = s.emp_id
                  )
 order by s.emp_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select s.emp_id, s.firstname, s.lastname, s.salary, s.department_id
  from salary s
 where s.salary = (select max(t.salary)
                     from salary t
                    where t.emp_id = s.emp_id
                  )
 order by s.emp_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select s.emp_id, s.firstname, s.lastname, s.salary, s.department_id
  from salary s
 where s.salary = (select max(t.salary)
                     from salary t
                    where t.emp_id = s.emp_id
                  )
 order by s.emp_id
;


# MySQL
# Write your MySQL query statement below
select s.emp_id, s.firstname, s.lastname, s.salary, s.department_id
  from salary s
 where s.salary = (select max(t.salary)
                     from salary t
                    where t.emp_id = s.emp_id
                  )
 order by s.emp_id
;


# Pandas
import pandas as pd

def find_latest_salaries(salary: pd.DataFrame) -> pd.DataFrame:
    df = salary.groupby('emp_id', as_index=0)['salary'].max()
    return salary.merge(df, how='inner', on=['emp_id', 'salary']).sort_values('emp_id')

