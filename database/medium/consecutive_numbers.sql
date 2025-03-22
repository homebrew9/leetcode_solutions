-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


# MySQL
# Write your MySQL query statement below
with t as (
select id, num,
       case when num = lag(num) over (order by id) and
                 num = lead(num) over (order by id) and
                 id = lag(id) over (order by id) + 1 and
                 id = lead(id) over (order by id) - 1
            then 'Y'
       end as valid
from logs
)
select distinct num as "ConsecutiveNums"
from t
where valid = 'Y'
;


# Pandas

