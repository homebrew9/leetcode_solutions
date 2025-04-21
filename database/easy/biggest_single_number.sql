-- Oracle
/* Write your PL/SQL query statement below */
with t (num, num_occurrences) as (
select num, count(*) over (partition by num) as num_occurrences
from MyNumbers
)
select max(num) as num
from t
where num_occurrences = 1
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

