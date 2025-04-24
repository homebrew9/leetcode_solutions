-- Oracle
/* Write your PL/SQL query statement below */
select actor_id, director_id
  from ActorDirector
 group by actor_id, director_id
having count(*) >= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select actor_id, director_id
  from ActorDirector
 group by actor_id, director_id
having count(*) >= 3
;


-- SQL Server


# MySQL
# Write your MySQL query statement below
select actor_id, director_id
from actordirector
group by actor_id, director_id
having count(*) >= 3
;


# Pandas

