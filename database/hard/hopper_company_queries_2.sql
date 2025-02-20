-- Oracle
/* Write your PL/SQL query statement below */
with year_iter (mth_num) as (
    select 1 from dual
    union all
    select yi.mth_num + 1
      from year_iter yi
     where yi.mth_num + 1 <= 12
),
t (mth_num, mth) as (
    select yi.mth_num, ADD_MONTHS(DATE'2020-01-01', yi.mth_num - 1) as mth
      from year_iter yi
),
t1 as (
select t.mth_num, t.mth, count(d.driver_id) as driver_cnt
from t
     left outer join drivers d on (trunc(d.join_date, 'mm') <= trunc(t.mth, 'mm'))
group by t.mth_num, t.mth
),
t2 as (
select trunc(r.requested_at, 'mm') as requested_at,
       count(distinct ar.driver_id) as accepted_rides
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by trunc(r.requested_at, 'mm')
)
select t1.mth_num as month,
       coalesce(case when t1.driver_cnt = 0 then 0
                     else round((t2.accepted_rides / t1.driver_cnt) * 100, 2)
                end,
                0
               ) as working_percentage
from t1
     left outer join t2 on (t2.requested_at = t1.mth)
order by t1.mth_num
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (mth_num, mth) as (
    select 1, '2020-01-01'::timestamp
    union all
    select t.mth_num + 1, t.mth + interval '1 month'
    from t
    where t.mth_num + 1 <= 12
),
t1 as (
select t.mth_num, t.mth, count(d.driver_id) as driver_cnt
from t
     left outer join drivers d on (date_trunc('month', d.join_date) <= t.mth)
group by t.mth_num, t.mth
),
t2 as (
select date_trunc('month', r.requested_at) as requested_at,
       count(distinct ar.driver_id) as accepted_rides
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by date_trunc('month', r.requested_at)
)
select t1.mth_num as month,
       coalesce(case when t1.driver_cnt = 0 then 0
                     else round((t2.accepted_rides::numeric / t1.driver_cnt::numeric) * 100, 2)
                end,
                0
               ) as working_percentage
from t1
     left outer join t2 on (t2.requested_at = t1.mth)
order by t1.mth_num
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (mth_num, mth) as (
    select 1, convert(datetime2, '2020-01-01')
    union all
    select t.mth_num + 1, DATEADD(MONTH, 1, t.mth)
    from t
    where t.mth_num + 1 <= 12
),
t1 as (
select t.mth_num, t.mth, count(d.driver_id) as driver_cnt
from t
     left outer join drivers d on (CONVERT(DATETIME, CONVERT(VARCHAR(7), d.join_date, 120) + '-01') <= t.mth)
group by t.mth_num, t.mth
),
t2 as (
select CONVERT(DATETIME, CONVERT(VARCHAR(7), r.requested_at, 120) + '-01') as requested_at,
       count(distinct ar.driver_id) as accepted_rides
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by CONVERT(DATETIME, CONVERT(VARCHAR(7), r.requested_at, 120) + '-01')
)
select t1.mth_num as month,
       coalesce(case when t1.driver_cnt = 0 then 0
                     else round((CONVERT(FLOAT, t2.accepted_rides) / CONVERT(FLOAT, t1.driver_cnt)) * 100, 2)
                end,
                0
               ) as working_percentage
from t1
     left outer join t2 on (t2.requested_at = t1.mth)
order by t1.mth_num
;


# MySQL
# Write your MySQL query statement below
with recursive t (mth_num, mth) as (
    select 1, '2020-01-01'
    union all
    select t.mth_num + 1, t.mth + interval 1 month
    from t
    where t.mth_num + 1 <= 12
),
t1 as (
select t.mth_num, t.mth, count(d.driver_id) as driver_cnt
from t
     left outer join drivers d on (str_to_date(DATE_FORMAT(d.join_date, '%Y-%m-01'), '%Y-%m-%d') <= t.mth)
group by t.mth_num, t.mth
),
t2 as (
select str_to_date(DATE_FORMAT(r.requested_at, '%Y-%m-01'), '%Y-%m-%d') as requested_at,
       count(distinct ar.driver_id) as accepted_rides
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by str_to_date(DATE_FORMAT(r.requested_at, '%Y-%m-01'), '%Y-%m-%d')
)
select t1.mth_num as month,
       coalesce(case when t1.driver_cnt = 0 then 0
                     else round((t2.accepted_rides / t1.driver_cnt) * 100, 2)
                end,
                0
               ) as working_percentage
from t1
     left outer join t2 on (t2.requested_at = t1.mth)
order by t1.mth_num
;

