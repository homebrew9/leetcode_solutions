-- Oracle
/* Write your PL/SQL query statement below */
select employee_id,
       case when mod(employee_id, 2) = 1 and name not like 'M%' then salary else 0 end as bonus
  from employees
 order by employee_id
;


-- PostgreSQL
select employee_id,
       case when mod(employee_id, 2) = 1 and name not like 'M%' then salary else 0 end as bonus
  from employees
 order by employee_id
;


-- SQL Server
select employee_id,
       case when employee_id % 2 = 1 and name not like 'M%' then salary else 0 end as bonus
  from employees
 order by employee_id
;


# MySQL
# Write your MySQL query statement below
select employee_id,
       case when mod(employee_id, 2) = 1 and substring(name,1,1) != 'M'
            then salary
            else 0
       end as bonus
from employees
order by employee_id
;


# Pandas
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # np.where is similar to Oracle's DECODE function
    employees['bonus'] = np.where(
                             (
                                  employees['employee_id']%2 == 1) & (~employees['name'].str.startswith('M')
                             ), employees['salary'], 0)
    return employees[['employee_id','bonus']].sort_values('employee_id')

