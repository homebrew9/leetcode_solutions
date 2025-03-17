-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select e.employee_id,
       e.needed_hours,
       coalesce(sum(ceil((out_time - in_time)*24*60))/60, 0) as total_hours
  from employees e
       left outer join logs a on (a.employee_id = e.employee_id)
 group by e.employee_id, e.needed_hours
)
select employee_id
from t
where total_hours < needed_hours
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- extract(epoch from dt1 - dt2) returns the difference in seconds,
-- convert to minutes and ceil them - this is for one session.
-- sum the ceil'ed minutes per session to get total minutes and
-- divide by 60 to get hours from total ceil'ed minutes!
with t as (
select e.employee_id,
       e.needed_hours,
       coalesce(
                  sum(
                        ceil(extract(epoch from out_time - in_time)/60)
                     )::numeric / 60,
                  0
               ) as total_hours
  from employees e
       left outer join logs a on (a.employee_id = e.employee_id)
 group by e.employee_id, e.needed_hours
)
select employee_id
from t
where total_hours < needed_hours
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select e.employee_id,
       e.needed_hours,
       coalesce(convert(float,
                        sum(
                             ceiling(convert(float, datediff(second, in_time, out_time))/60)
                           )
                       ) / 60,
                0
               ) as total_hours
  from employees e
       left outer join logs a on (a.employee_id = e.employee_id)
 group by e.employee_id, e.needed_hours
)
select employee_id
from t
where total_hours < needed_hours
;


# MySQL
# Write your MySQL query statement below
with t as (
select e.employee_id,
       e.needed_hours,
       coalesce(
                sum(
                     ceiling(timestampdiff(second, in_time, out_time)/60)
                   ) / 60,
                0
               ) as total_hours
  from employees e
       left outer join logs a on (a.employee_id = e.employee_id)
 group by e.employee_id, e.needed_hours
)
select employee_id
from t
where total_hours < needed_hours
;


# Pandas

