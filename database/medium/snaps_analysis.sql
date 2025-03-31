-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


# MySQL
# Write your MySQL query statement below
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


# Pandas

