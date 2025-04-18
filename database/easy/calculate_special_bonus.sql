-- Oracle
/* Write your PL/SQL query statement below */
select employee_id,
       case when mod(employee_id, 2) = 1 and name not like 'M%' then salary else 0 end as bonus
  from employees
 order by employee_id
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

