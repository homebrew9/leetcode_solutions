-- Oracle
/* Write your PL/SQL query statement below */
select e.reports_to as employee_id, e1.name, count(*) as reports_count, round(avg(e.age)) as average_age
from employees e
     inner join employees e1 on (e1.employee_id = e.reports_to)
group by e.reports_to, e1.name
order by e.reports_to
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

