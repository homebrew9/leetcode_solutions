-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select user_id, activity_type, round(avg(convert(float, activity_duration)), 2) as avg_duration
      from UserActivity
     group by user_id, activity_type
)
select user_id,
       max(case when activity_type = 'free_trial' then avg_duration end) as trial_avg_duration,
       max(case when activity_type = 'paid' then avg_duration end) as paid_avg_duration
  from t
 group by user_id
 having max(case when activity_type = 'paid' then avg_duration end) is not null
 order by user_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select user_id, activity_type, round(avg(activity_duration), 2) as avg_duration
      from UserActivity
     group by user_id, activity_type
)
select user_id,
       max(case when activity_type = 'free_trial' then avg_duration end) as trial_avg_duration,
       max(case when activity_type = 'paid' then avg_duration end) as paid_avg_duration
  from t
 group by user_id
 having max(case when activity_type = 'paid' then avg_duration end) is not null
 order by user_id
;


# Pandas

