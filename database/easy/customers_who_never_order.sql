-- Oracle
/* Write your PL/SQL query statement below */
select c.name as customers
  from customers c
 where not exists (select null
                     from orders o
                    where o.customerId = c.id
                  )
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

