-- Oracle
/* Write your PL/SQL query statement below */
with t (airport_id, flights_count) as (
select x.airport_id, sum(x.flights_count) as flights_count
from (
    select departure_airport as airport_id, flights_count from flights
    union all
    select arrival_airport as airport_id, flights_count from flights
) x
group by x.airport_id
)
select airport_id
from t
where flights_count = (select max(flights_count) from t)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (airport_id, flights_count) as (
select x.airport_id, sum(x.flights_count) as flights_count
from (
    select departure_airport as airport_id, flights_count from flights
    union all
    select arrival_airport as airport_id, flights_count from flights
) x
group by x.airport_id
)
select airport_id
from t
where flights_count = (select max(flights_count) from t)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (airport_id, flights_count) as (
select x.airport_id, sum(x.flights_count) as flights_count
from (
    select departure_airport as airport_id, flights_count from flights
    union all
    select arrival_airport as airport_id, flights_count from flights
) x
group by x.airport_id
)
select airport_id
from t
where flights_count = (select max(flights_count) from t)
;


# MySQL
# Write your MySQL query statement below
with t (airport_id, flights_count) as (
select x.airport_id, sum(x.flights_count) as flights_count
from (
    select departure_airport as airport_id, flights_count from flights
    union all
    select arrival_airport as airport_id, flights_count from flights
) x
group by x.airport_id
)
select airport_id
from t
where flights_count = (select max(flights_count) from t)
;


# Pandas
import pandas as pd

def airport_with_most_traffic(flights: pd.DataFrame) -> pd.DataFrame:
    df = ( pd.concat([
               flights[['departure_airport', 'flights_count']].rename(columns={'departure_airport':'airport_id'}),
               flights[['arrival_airport', 'flights_count']].rename(columns={'arrival_airport':'airport_id'})
           ])
         )
    df = df.groupby('airport_id', as_index=False)['flights_count'].sum()
    return df[df['flights_count'] == df['flights_count'].max()][['airport_id']]

