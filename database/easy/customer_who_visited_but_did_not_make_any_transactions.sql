-- Oracle
/* Write your PL/SQL query statement below */
select v.customer_id as "customer_id", count(v.visit_id) as "count_no_trans"
from visits v
where not exists (select null from transactions t where t.visit_id = v.visit_id)
group by v.customer_id
;


-- PostgreSQL


-- SQL Server


# MySQL
# Write your MySQL query statement below
select v.customer_id, count(v.visit_id) as count_no_trans
from visits v
where not exists (select null from transactions t where t.visit_id = v.visit_id)
group by v.customer_id
;


# Pandas

