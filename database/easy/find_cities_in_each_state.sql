-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select state, string_agg(city, ', ') within group (order by city) as cities
from cities
group by state
order by state
;


# MySQL


# Pandas

