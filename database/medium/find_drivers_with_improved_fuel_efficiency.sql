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
/* Write your T-SQL query statement below */
with t_first_half as (
    select driver_id, avg(distance_km / fuel_consumed) as first_half_avg
    from trips
    where month(trip_date) between 1 and 6
    group by driver_id
),
t_second_half as (
    select driver_id, avg(distance_km / fuel_consumed) as second_half_avg
    from trips
    where month(trip_date) between 7 and 12
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


# MySQL
# Write your MySQL query statement below
with t_first_half as (
    select driver_id, avg(distance_km / fuel_consumed) as first_half_avg
    from trips
    where month(trip_date) between 1 and 6
    group by driver_id
),
t_second_half as (
    select driver_id, avg(distance_km / fuel_consumed) as second_half_avg
    from trips
    where month(trip_date) between 7 and 12
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


# Pandas
import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips['trip_date'] = pd.to_datetime(trips['trip_date'])
    trips['month'] = trips['trip_date'].dt.strftime('%m').astype(int)
    trips['fuel_efficiency'] = trips['distance_km'] / trips['fuel_consumed']
    df_first_half = ( trips
                     .query('1 <= month <= 6')
                     .groupby('driver_id', as_index=0)
                     .agg(first_half_avg=('fuel_efficiency', 'mean'))
                    )
    df_second_half = ( trips
                      .query('7 <= month <= 12')
                      .groupby('driver_id', as_index=0)
                      .agg(second_half_avg=('fuel_efficiency', 'mean'))
                     )
    df = ( df_first_half
          .merge(df_second_half, how='inner', on='driver_id')
          .query('second_half_avg > first_half_avg')
         )
    df['efficiency_improvement'] = df['second_half_avg'] - df['first_half_avg']
    df['first_half_avg'] = round(df['first_half_avg'], 2)
    df['second_half_avg'] = round(df['second_half_avg'], 2)
    df['efficiency_improvement'] = round(df['efficiency_improvement'], 2)
    return ( drivers
            .merge(df, how='inner', on='driver_id')
            .sort_values(by=['efficiency_improvement', 'driver_name'], ascending=[False, True])
           )

