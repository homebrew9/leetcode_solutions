-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id1, user_id2) as (
    select distinct user_id1, user_id2 from (
        select user_id1, user_id2 from friends
        union all
        select user_id2, user_id1 from friends
    )
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id1, user_id2) as (
    select distinct user_id1, user_id2 from (
        select user_id1, user_id2 from friends
        union all
        select user_id2, user_id1 from friends
    )
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id1, user_id2) as (
    select distinct x.user_id1, x.user_id2
      from (
                select user_id1, user_id2 from friends
                union all
                select user_id2, user_id1 from friends
           ) as x
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


# MySQL
# Write your MySQL query statement below
with t (user_id1, user_id2) as (
    select distinct x.user_id1, x.user_id2
      from (
                select user_id1, user_id2 from friends
                union all
                select user_id2, user_id1 from friends
           ) as x
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


# Pandas

