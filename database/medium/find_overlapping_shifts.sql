-- Oracle
/* Write your PL/SQL query statement below */
select e1.employee_id, count(*) as overlapping_shifts
  from EmployeeShifts e1
       inner join EmployeeShifts e2
       on (e1.employee_id = e2.employee_id and
           e2.start_time > e1.start_time and
           e2.start_time < e1.end_time
          )
 group by e1.employee_id
 order by 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e1.employee_id, count(*) as overlapping_shifts
  from EmployeeShifts e1
       inner join EmployeeShifts e2
       on (e1.employee_id = e2.employee_id and
           e2.start_time > e1.start_time and
           e2.start_time < e1.end_time
          )
 group by e1.employee_id
 order by 1
;


-- SQL Server
/* Write your T-SQL query statement below */
select e1.employee_id, count(*) as overlapping_shifts
  from EmployeeShifts e1
       inner join EmployeeShifts e2
       on (e1.employee_id = e2.employee_id and
           e2.start_time > e1.start_time and
           e2.start_time < e1.end_time
          )
 group by e1.employee_id
 order by 1
;


# MySQL
# Write your MySQL query statement below
select e1.employee_id, count(*) as overlapping_shifts
  from EmployeeShifts e1
       inner join EmployeeShifts e2
       on (e1.employee_id = e2.employee_id and
           e2.start_time > e1.start_time and
           e2.start_time < e1.end_time
          )
 group by e1.employee_id
 order by 1
;


# Pandas
import pandas as pd

def find_overlapping_shifts(employee_shifts: pd.DataFrame) -> pd.DataFrame:
    return ( employee_shifts
            .merge(employee_shifts, how='inner', on='employee_id')
            .query('start_time_y > start_time_x and start_time_y < end_time_x')
            .groupby('employee_id', as_index=0)['start_time_y']
            .count()
            .rename(columns={'start_time_y': 'overlapping_shifts'})
            .sort_values('employee_id')
           )

