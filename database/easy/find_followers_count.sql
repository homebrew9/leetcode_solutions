-- Oracle
/* Write your PL/SQL query statement below */
select user_id, count(*) as "followers_count"
from followers
group by user_id
order by user_id
;


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
select user_id, count(*) as followers_count
from followers
group by user_id
order by user_id
;


# Pandas

