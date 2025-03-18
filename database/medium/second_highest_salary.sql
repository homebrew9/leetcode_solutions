-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
      from dual
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select id, salary, dense_rank() over (order by salary desc) as drnk
      from employee
),
d as (
    select 2 as drnk
)
select distinct t.salary as SecondHighestSalary
  from d
       left outer join t on (t.drnk = d.drnk)
;


# Pandas

