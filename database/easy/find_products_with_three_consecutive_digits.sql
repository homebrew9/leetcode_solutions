-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select product_id, name
from products
where name like '%[0-9][0-9][0-9]%'
and name not like '%[0-9][0-9][0-9][0-9]%'
order by product_id
;


# MySQL


# Pandas

