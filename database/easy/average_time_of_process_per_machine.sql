-- Oracle
/* Write your PL/SQL query statement below */
with t (machine_id, process_id, start_ts, end_ts) as (
    select machine_id, process_id,
           max(decode(activity_type, 'start', timestamp)) as start_ts,
           max(decode(activity_type, 'end', timestamp)) as end_ts
      from Activity
     group by machine_id, process_id
)
select machine_id, round(avg(end_ts - start_ts), 3) as processing_time
from t
group by machine_id
;


-- PostgreSQL


-- SQL Server


# MySQL


# Pandas

