-- Oracle
/* Write your PL/SQL query statement below */
select distinct x.driver_id,
                (select count(*) from rides y where y.passenger_id = x.driver_id) as cnt
from rides x
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select distinct x.driver_id,
                (select count(*) from rides y where y.passenger_id = x.driver_id) as cnt
from rides x
;


-- SQL Server
/* Write your T-SQL query statement below */
select distinct x.driver_id,
                (select count(*) from rides y where y.passenger_id = x.driver_id) as cnt
from rides x
;


# MySQL
# Write your MySQL query statement below
select distinct x.driver_id,
                (select count(*) from rides y where y.passenger_id = x.driver_id) as cnt
from rides x
;


# Pandas
import pandas as pd

def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    df = ( rides
          .groupby('passenger_id', as_index=False)['ride_id']
          .count()
          .rename(columns={'passenger_id':'driver_id', 'ride_id':'cnt'})
         )
    df1 = ( rides
           .merge(df, how='left', on='driver_id')
           .fillna(0)
           .astype(int)[['driver_id', 'cnt']]
           .drop_duplicates()
          )
    return df1

