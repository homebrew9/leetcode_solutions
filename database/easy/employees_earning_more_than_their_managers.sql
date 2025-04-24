-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
SELECT e.name AS Employee
FROM Employee e
     INNER JOIN Employee m ON (m.id = e.managerId)
WHERE e.salary > m.salary
;


# MySQL


# Pandas

