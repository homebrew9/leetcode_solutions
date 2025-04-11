-- Oracle
/* Write your PL/SQL query statement below */
with t (dep_id, employee_count) as (
select dep_id, count(*) as employee_count
from employees
group by dep_id
),
t1 (dep_id, employee_count, max_emp_count) as (
select dep_id, employee_count,
       max(employee_count) over () as max_emp_count
from t
)
select e.emp_name as manager_name, e.dep_id
from employees e
     inner join t1 on (t1.dep_id = e.dep_id)
where e.position = 'Manager'
and t1.employee_count = t1.max_emp_count
order by e.dep_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (dep_id, employee_count) as (
select dep_id, count(*) as employee_count
from employees
group by dep_id
),
t1 (dep_id, employee_count, max_emp_count) as (
select dep_id, employee_count,
       max(employee_count) over () as max_emp_count
from t
)
select e.emp_name as manager_name, e.dep_id
from employees e
     inner join t1 on (t1.dep_id = e.dep_id)
where e.position = 'Manager'
and t1.employee_count = t1.max_emp_count
order by e.dep_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (dep_id, employee_count) as (
select dep_id, count(*) as employee_count
from employees
group by dep_id
),
t1 (dep_id, employee_count, max_emp_count) as (
select dep_id, employee_count,
       max(employee_count) over () as max_emp_count
from t
)
select e.emp_name as manager_name, e.dep_id
from employees e
     inner join t1 on (t1.dep_id = e.dep_id)
where e.position = 'Manager'
and t1.employee_count = t1.max_emp_count
order by e.dep_id
;


# MySQL
# Write your MySQL query statement below
with t (dep_id, employee_count) as (
select dep_id, count(*) as employee_count
from employees
group by dep_id
),
t1 (dep_id, employee_count, max_emp_count) as (
select dep_id, employee_count,
       max(employee_count) over () as max_emp_count
from t
)
select e.emp_name as manager_name, e.dep_id
from employees e
     inner join t1 on (t1.dep_id = e.dep_id)
where e.position = 'Manager'
and t1.employee_count = t1.max_emp_count
order by e.dep_id
;


# Pandas
import pandas as pd

def find_manager(employees: pd.DataFrame) -> pd.DataFrame:
    df = ( employees
          .groupby('dep_id', as_index=0)['emp_id']
          .count()
          .rename(columns={'emp_id': 'emp_count'})
         )
    df['rnk'] = df['emp_count'].rank(method='dense', ascending=False)
    largest_dept = df[df['rnk']==1]['dep_id']
    return ( employees[ (employees['dep_id'].isin(largest_dept))
                        &
                        (employees['position']=='Manager')
                      ][['emp_name','dep_id']]
            .rename(columns={'emp_name': 'manager_name'})
            .sort_values('dep_id')
           )

