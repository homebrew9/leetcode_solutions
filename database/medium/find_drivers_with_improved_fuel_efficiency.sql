-- Oracle
/* Write your PL/SQL query statement below */
with t_first_half as (
    select driver_id, avg(distance_km / fuel_consumed) as first_half_avg
    from trips
    where to_number(to_char(trip_date, 'mm')) between 1 and 6
    group by driver_id
),
t_second_half as (
    select driver_id, avg(distance_km / fuel_consumed) as second_half_avg
    from trips
    where to_number(to_char(trip_date, 'mm')) between 7 and 12
    group by driver_id
)
select f.driver_id, d.driver_name,
       round(f.first_half_avg, 2) as first_half_avg,
       round(s.second_half_avg, 2) as second_half_avg,
       round(s.second_half_avg - f.first_half_avg, 2) as efficiency_improvement
  from t_first_half f
       inner join t_second_half s on (s.driver_id = f.driver_id)
       inner join drivers d on (d.driver_id = f.driver_id)
 where s.second_half_avg > f.first_half_avg
 order by efficiency_improvement desc, driver_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t_first_half as (
    select driver_id, avg(distance_km / fuel_consumed) as first_half_avg
    from trips
    where to_char(trip_date, 'mm')::int between 1 and 6
    group by driver_id
),
t_second_half as (
    select driver_id, avg(distance_km / fuel_consumed) as second_half_avg
    from trips
    where to_char(trip_date, 'mm')::int between 7 and 12
    group by driver_id
)
select f.driver_id, d.driver_name,
       round(f.first_half_avg, 2) as first_half_avg,
       round(s.second_half_avg, 2) as second_half_avg,
       round(s.second_half_avg - f.first_half_avg, 2) as efficiency_improvement
  from t_first_half f
       inner join t_second_half s on (s.driver_id = f.driver_id)
       inner join drivers d on (d.driver_id = f.driver_id)
 where s.second_half_avg > f.first_half_avg
 order by efficiency_improvement desc, driver_name
;




-- SQL Server


# MySQL


# Pandas

