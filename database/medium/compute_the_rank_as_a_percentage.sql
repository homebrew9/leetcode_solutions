-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select student_id, department_id, mark,
       rank() over (partition by department_id order by mark desc) as rnk,
       count(*) over (partition by department_id) as student_count
from students
)
select student_id, department_id,
       round( case when student_count = 1 then 0
                   else convert(float, ((rnk - 1) * 100) )
                        /
                        convert(float, (student_count - 1) )
              end,
              2
            ) as percentage
from t
;


# MySQL
# Write your MySQL query statement below
-- Write your PostgreSQL query statement below
with t as (
select student_id, department_id, mark,
       rank() over (partition by department_id order by mark desc) as rnk,
       count(*) over (partition by department_id) as student_count
from students
)
select student_id, department_id,
       round( case when student_count = 1 then 0
                   else ((rnk - 1) * 100) / (student_count - 1)
              end,
              2
            ) as percentage
from t
;


# Pandas


