-- Oracle
/* Write your PL/SQL query statement below */
select to_char(event_day, 'yyyy-mm-dd') as day,
       emp_id,
       sum(out_time - in_time) as total_time
  from employees
 group by event_day, emp_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select to_char(event_day, 'YYYY-MM-DD') as "day",
       emp_id as "emp_id",
       sum(out_time - in_time) as "total_time"
  from employees
 group by to_char(event_day, 'YYYY-MM-DD'), emp_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select convert(varchar, convert(date, event_day), 120) as day,
       emp_id as emp_id,
       sum(out_time - in_time) as total_time
  from employees
 group by convert(varchar, convert(date, event_day), 120), emp_id
;


# MySQL
# Write your MySQL query statement below
select DATE_FORMAT(event_day, '%Y-%m-%d') as day,
       emp_id as emp_id,
       sum(out_time - in_time) as total_time
  from employees
 group by DATE_FORMAT(event_day, '%Y-%m-%d'), emp_id
;


# Pandas
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['duration'] = employees['out_time'] - employees['in_time']
    return (  employees.groupby(by=['event_day','emp_id'], as_index=False)
              .agg(total_time = ('duration', 'sum'))
              .rename(columns={'event_day':'day'})
           )

