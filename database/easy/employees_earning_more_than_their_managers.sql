-- Oracle
/* Write your PL/SQL query statement below */
select e.name as "Employee"
  from employee e
       inner join employee m
       on (e.managerid = m.id and e.salary > m.salary)
;


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
SELECT e.name AS Employee
FROM Employee e
     INNER JOIN Employee m ON (m.id = e.managerId)
WHERE e.salary > m.salary
;


# MySQL
# Write your MySQL query statement below
select e.name as Employee
  from employee e
       inner join employee m on (m.id = e.managerId)
 where e.salary > m.salary
;


# Pandas

