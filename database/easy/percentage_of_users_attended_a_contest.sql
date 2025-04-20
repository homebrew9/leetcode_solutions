-- Oracle
/* Write your PL/SQL query statement below */
select r.contest_id, round(count(*)/u.user_count * 100, 2) as percentage
from register r
     cross join (select count(*) as user_count from users) u
group by r.contest_id, u.user_count
order by percentage desc, r.contest_id
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

