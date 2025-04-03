-- Oracle
/* Write your PL/SQL query statement below */
with t (dept_id, dept_name, student_number) as (
select d.dept_id, d.dept_name, count(student_id) as student_number
from department d
     left outer join student s on (s.dept_id = d.dept_id)
group by d.dept_id, d.dept_name
)
select dept_name, student_number
from t
order by student_number desc, dept_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (dept_id, dept_name, student_number) as (
select d.dept_id, d.dept_name, count(student_id) as student_number
from department d
     left outer join student s on (s.dept_id = d.dept_id)
group by d.dept_id, d.dept_name
)
select dept_name, student_number
from t
order by student_number desc, dept_name
;


-- SQL Server


# MySQL


# Pandas

