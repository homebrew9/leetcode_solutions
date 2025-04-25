-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (employee_id, department_id, primary_flag, dept_count) as (
    select employee_id, department_id, primary_flag,
           count(*) over (partition by employee_id) as dept_count
      from employee
)
select employee_id, department_id
  from t
 where dept_count = 1
    or primary_flag = 'Y'
;


-- SQL Server


# MySQL


# Pandas

