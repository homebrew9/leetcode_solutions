-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select v.fuel_type, v.driver_id, d.accidents, round(avg(t.rating), 2) as rating, sum(t.distance) as distance
      from vehicles v
           inner join trips t on (t.vehicle_id = v.vehicle_id)
           inner join drivers d on (v.driver_id = d.driver_id)
     group by v.fuel_type, v.driver_id, d.accidents
)
,
t1 as (
    select fuel_type, driver_id, accidents, rating, distance,
           dense_rank() over (partition by fuel_type order by rating desc, distance desc, accidents) as drnk
      from t
)
select fuel_type, driver_id, rating, distance
  from t1
 where drnk = 1
 order by fuel_type
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select v.fuel_type, v.driver_id, d.accidents, round(avg(t.rating), 2) as rating, sum(t.distance) as distance
      from vehicles v
           inner join trips t on (t.vehicle_id = v.vehicle_id)
           inner join drivers d on (v.driver_id = d.driver_id)
     group by v.fuel_type, v.driver_id, d.accidents
)
,
t1 as (
    select fuel_type, driver_id, accidents, rating, distance,
           dense_rank() over (partition by fuel_type order by rating desc, distance desc, accidents) as drnk
      from t
)
select fuel_type, driver_id, rating, distance
  from t1
 where drnk = 1
 order by fuel_type
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select v.fuel_type, v.driver_id, d.accidents,
           round(avg(convert(float, t.rating)), 2) as rating,
           sum(t.distance) as distance
      from vehicles v
           inner join trips t on (t.vehicle_id = v.vehicle_id)
           inner join drivers d on (v.driver_id = d.driver_id)
     group by v.fuel_type, v.driver_id, d.accidents
)
,
t1 as (
    select fuel_type, driver_id, accidents, rating, distance,
           dense_rank() over (partition by fuel_type order by rating desc, distance desc, accidents) as drnk
      from t
)
select fuel_type, driver_id, rating, distance
  from t1
 where drnk = 1
 order by fuel_type
;


# MySQL
# Write your MySQL query statement below
with t as (
    select v.fuel_type, v.driver_id, d.accidents,
           round(avg(t.rating), 2) as rating, sum(t.distance) as distance
      from vehicles v
           inner join trips t on (t.vehicle_id = v.vehicle_id)
           inner join drivers d on (v.driver_id = d.driver_id)
     group by v.fuel_type, v.driver_id, d.accidents
)
,
t1 as (
    select fuel_type, driver_id, accidents, rating, distance,
           dense_rank() over (partition by fuel_type order by rating desc, distance desc, accidents) as drnk
      from t
)
select fuel_type, driver_id, rating, distance
  from t1
 where drnk = 1
 order by fuel_type
;


# Pandas
import pandas as pd

def get_top_performing_drivers(drivers: pd.DataFrame, vehicles: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    df = ( drivers
          .merge(vehicles, how='inner', on='driver_id')
          .merge(trips, how='inner', on='vehicle_id')
          .groupby(['fuel_type', 'driver_id', 'accidents'], as_index=0)
          .agg({'rating': 'mean', 'distance': 'sum'})
         )
    df['rating'] = round(df['rating'], 2)
    # Great technique for dense rank with partition by and order by on multiple columns:
    # https://stackoverflow.com/questions/76309894/pandas-group-by-dense-rank-partitioned-by-multiple-columns
    df['rnk'] = ( df
                 .sort_values(['fuel_type','rating','distance','accidents'], ascending=[True,False,False,True])
                 .groupby('fuel_type')
                 .cumcount()
                 .add(1)
                )
    return df[df['rnk']==1][['fuel_type','driver_id','rating','distance']]

