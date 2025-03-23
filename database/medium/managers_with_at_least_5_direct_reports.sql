-- Oracle
/* Write your PL/SQL query statement below */
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


-- SQL Server
/* Write your T-SQL query statement below */
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


# MySQL
# Write your MySQL query statement below
select e1.name
from employee e
     inner join employee e1 on (e1.id = e.managerId)
group by e.managerId, e1.name
having count(*) >= 5
;


# Pandas

