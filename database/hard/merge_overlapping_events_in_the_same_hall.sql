-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select hall_id, start_day, end_day,
       max(end_day) over (partition by hall_id
                          order by start_day, end_day
                          rows between unbounded preceding and 1 preceding
                         ) as max_ed_so_far,
       case when start_day > coalesce(
                                 max(end_day) over (
                                     partition by hall_id
                                     order by start_day, end_day
                                     rows between unbounded preceding and 1 preceding
                                 ),
                                 start_day-1
                             )
            then 1
            else 0
       end as interval_start
from hallevents
)
,
t1 as (
select hall_id, start_day, end_day, max_ed_so_far, interval_start,
       sum(interval_start) over (order by hall_id, start_day, end_day
                                 rows between unbounded preceding and current row
                                ) as interval_group
from t
)
select hall_id,
       to_char(min(start_day), 'YYYY-MM-DD') as start_day,
       to_char(max(end_day), 'YYYY-MM-DD') as end_day
from t1
group by hall_id, interval_group
order by hall_id, interval_group
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select hall_id, start_day, end_day,
       max(end_day) over (partition by hall_id
                          order by start_day, end_day
                          rows between unbounded preceding and 1 preceding
                         ) as max_ed_so_far,
       case when start_day > coalesce(
                                 max(end_day) over (
                                     partition by hall_id
                                     order by start_day, end_day
                                     rows between unbounded preceding and 1 preceding
                                 ),
                                 DATEADD(DAY, -1, start_day)
                             )
            then 1
            else 0
       end as interval_start
from hallevents
)
,
t1 as (
select hall_id, start_day, end_day, max_ed_so_far, interval_start,
       sum(interval_start) over (order by hall_id, start_day, end_day
                                 rows between unbounded preceding and current row
                                ) as interval_group
from t
)
select hall_id,
       min(start_day) as start_day,
       max(end_day) as end_day
from t1
group by hall_id, interval_group
order by hall_id, interval_group
;


# MySQL
# Write your MySQL query statement below
with t as (
select hall_id, start_day, end_day,
       max(end_day) over (partition by hall_id
                          order by start_day, end_day
                          rows between unbounded preceding and 1 preceding
                         ) as max_ed_so_far,
       case when max(end_day) over (partition by hall_id
                          order by start_day, end_day
                          rows between unbounded preceding and 1 preceding
                         ) is null
                 or
                 start_day > max(end_day) over (
                                 partition by hall_id
                                 order by start_day, end_day
                                 rows between unbounded preceding and 1 preceding
                             )
            then 1
            else 0
       end as interval_start
from hallevents
)
,
t1 as (
select hall_id, start_day, end_day, max_ed_so_far, interval_start,
       sum(interval_start) over (order by hall_id, start_day, end_day
                                 rows between unbounded preceding and current row
                                ) as interval_group
from t
)
select hall_id,
       min(start_day) as start_day,
       max(end_day) as end_day
from t1
group by hall_id, interval_group
order by hall_id, interval_group
;

