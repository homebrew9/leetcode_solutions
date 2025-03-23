-- Oracle
/* Write your PL/SQL query statement below */
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
order by b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
order by b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


# MySQL
# Write your MySQL query statement below
with t as (
select b.bus_id, b.arrival_time, count(passenger_id) as cnt
from buses b
     left outer join passengers p on (p.arrival_time <= b.arrival_time)
group by b.bus_id, b.arrival_time
order by b.arrival_time
)
select bus_id,
       cnt - coalesce(lag(cnt) over (order by arrival_time), 0) as passengers_cnt
from t
order by bus_id
;


# Pandas
import pandas as pd

def count_passengers_in_bus(buses: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    buses.sort_values('arrival_time', inplace=True)
    buses['prev_arrival_time'] = buses['arrival_time'].shift(1).fillna(-1)
    df = ( buses
          .merge(passengers, how='cross')
          .query('arrival_time_y > prev_arrival_time and arrival_time_y <= arrival_time_x')
          .groupby('bus_id', as_index=0)['passenger_id']
          .count()
          .rename(columns={'passenger_id': 'passengers_cnt'})
         )
    return ( buses[['bus_id']]
            .drop_duplicates()
            .merge(df, how='left', on='bus_id')
            .fillna(0)
            .sort_values('bus_id')
           )

