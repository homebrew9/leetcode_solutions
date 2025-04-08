-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
-- Old-style
select s1.user_id, s1.steps_date,
       round(CONVERT(FLOAT, (s1.steps_count+s2.steps_count+s3.steps_count)) / 3.0, 2) as rolling_average
from steps s1
     inner join steps s2 on (s2.user_id = s1.user_id and s2.steps_date = DATEADD(DAY, -1, s1.steps_date))
     inner join steps s3 on (s3.user_id = s2.user_id and s3.steps_date = DATEADD(DAY, -1, s2.steps_date))
order by s1.user_id, s1.steps_date
;


# MySQL
# Write your MySQL query statement below
-- Old-style
select s1.user_id, s1.steps_date,
       round((s1.steps_count+s2.steps_count+s3.steps_count)/3, 2) as rolling_average
from steps s1
     inner join steps s2 on (s2.user_id = s1.user_id and s2.steps_date = DATE_SUB(s1.steps_date, INTERVAL 1 DAY))
     inner join steps s3 on (s3.user_id = s2.user_id and s3.steps_date = DATE_SUB(s2.steps_date, INTERVAL 1 DAY))
order by s1.user_id, s1.steps_date
;


# Pandas

