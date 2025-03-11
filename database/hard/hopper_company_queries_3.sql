-- Oracle
/* Write your PL/SQL query statement below */
with t_year (month_num) as (
    select 1 as month_num
      from dual
    union all
    select ty.month_num + 1
      from t_year ty
     where ty.month_num + 1 <= 12
),
t (month_num, month) as (
select ty.month_num, add_months(DATE'2020-01-01', ty.month_num - 1) as month
from t_year ty
),
t1 as (
select trunc(r.requested_at, 'mm') as month,
       sum(ar.ride_distance) as total_ride_distance,
       sum(ar.ride_duration) as total_ride_duration
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by trunc(r.requested_at, 'mm')
),
t2 as (
select t.month_num, t.month,
       coalesce(total_ride_distance, 0) as total_ride_distance,
       coalesce(total_ride_duration, 0) as total_ride_duration
from t
     left outer join t1 on (t1.month = t.month)
),
t3 as (
select month_num, month,
       sum(total_ride_distance) over (order by month rows between current row and 2 following) / 3 as avg_ride_distance,
       sum(total_ride_duration) over (order by month rows between current row and 2 following) / 3 as avg_ride_duration
from t2
)
select month_num as month,
       round(avg_ride_distance, 2) as average_ride_distance,
       round(avg_ride_duration, 2) as average_ride_duration
from t3
where month_num <= 10
order by month_num
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with recursive t (year_month, month) as (
  select '2020-01-01'::timestamp as year_month, 1 as month
  union all
  select t.year_month + interval '1 month', t.month + 1
  from t
  where t.month + 1 <= 12
),
t1 (year_month, ride_distance, ride_duration) as (
select date_trunc('month', r.requested_at) as year_month, ar.ride_distance, ar.ride_duration
from rides r
     inner join AcceptedRides ar on (ar.ride_id = r.ride_id)
)
select t.month,
       coalesce(round(sum(t1.ride_distance)::numeric/3, 2), 0) as average_ride_distance,
       coalesce(round(sum(t1.ride_duration)::numeric/3, 2), 0) as average_ride_duration
from t
     left outer join t1 on (t1.year_month between t.year_month and t.year_month + interval '2 month')
where t.year_month between '2020-01-01'::timestamp and '2020-10-01'::timestamp
group by t.month
order by month
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (month_num, month) as (
    select 1 as month_num, CONVERT(DATE, '2020-01-01') as month
    union all
    select t.month_num + 1, DATEADD(MONTH, 1, t.month)
      from t
     where t.month_num + 1 <= 12
),
t1 as (
select CONVERT(DATETIME, CONVERT(VARCHAR(7), r.requested_at, 120) + '-01') as month,
       sum(ar.ride_distance) as total_ride_distance,
       sum(ar.ride_duration) as total_ride_duration
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by CONVERT(DATETIME, CONVERT(VARCHAR(7), r.requested_at, 120) + '-01')
),
t2 as (
select t.month_num, t.month,
       coalesce(total_ride_distance, 0) as total_ride_distance,
       coalesce(total_ride_duration, 0) as total_ride_duration
from t
     left outer join t1 on (t1.month = t.month)
),
t3 as (
select month_num, month,
       sum(total_ride_distance) over (order by month rows between current row and 2 following) / 3.0 as avg_ride_distance,
       sum(total_ride_duration) over (order by month rows between current row and 2 following) / 3.0 as avg_ride_duration
from t2
)
select month_num as month,
       round(avg_ride_distance, 2) as average_ride_distance,
       round(avg_ride_duration, 2) as average_ride_duration
from t3
where month_num <= 10
order by month_num
;


# MySQL
# Write your MySQL query statement below
with recursive t (month_num, month) as (
    select 1 as month_num, '2020-01-01' as month
    union all
    select t.month_num + 1, t.month + INTERVAL 1 MONTH
      from t
     where t.month_num + 1 <= 12
),
t1 as (
select str_to_date(DATE_FORMAT(r.requested_at, '%Y-%m-01'), '%Y-%m-%d') as month,
       sum(ar.ride_distance) as total_ride_distance,
       sum(ar.ride_duration) as total_ride_duration
from rides r
     inner join acceptedrides ar on (ar.ride_id = r.ride_id)
group by str_to_date(DATE_FORMAT(r.requested_at, '%Y-%m-01'), '%Y-%m-%d')
),
t2 as (
select t.month_num, t.month,
       coalesce(total_ride_distance, 0) as total_ride_distance,
       coalesce(total_ride_duration, 0) as total_ride_duration
from t
     left outer join t1 on (t1.month = t.month)
),
t3 as (
select month_num, month,
       sum(total_ride_distance) over (order by month rows between current row and 2 following) / 3 as avg_ride_distance,
       sum(total_ride_duration) over (order by month rows between current row and 2 following) / 3 as avg_ride_duration
from t2
)
select month_num as month,
       round(avg_ride_distance, 2) as average_ride_distance,
       round(avg_ride_duration, 2) as average_ride_duration
from t3
where month_num <= 10
order by month_num
;


# Pandas
import pandas as pd

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    rides['mth'] = rides['requested_at'].dt.strftime('%Y-%m-01')
    df = ( rides
          .merge(accepted_rides, how='inner', on='ride_id')
          .groupby('mth',as_index=False)
          .agg(ride_distance=('ride_distance', 'sum'), ride_duration=('ride_duration', 'sum'))
         )
    all_months = pd.DataFrame(data={'month': range(1,13)})
    all_months['mth'] = '2020-' + all_months['month'].astype(str).str.zfill(2) + '-01'
    df1 = all_months.merge(df, how='left', on='mth').fillna(0)
    df1['average_ride_distance'] = round( (df1['ride_distance'] +
                                           df1.shift(-1)['ride_distance'] +
                                           df1.shift(-2)['ride_distance']
                                          ) / 3,
                                          2
                                        )
    df1['average_ride_duration'] = round( (df1['ride_duration'] +
                                           df1.shift(-1)['ride_duration'] +
                                           df1.shift(-2)['ride_duration']
                                          ) / 3,
                                          2
                                        )
    return df1[['month','average_ride_distance','average_ride_duration']].query('month <= 10')

