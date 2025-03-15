-- Oracle
/* Write your PL/SQL query statement below */
SELECT f.flight_id,
       LEAST(f.capacity, COUNT(p.passenger_id)) AS booked_cnt, 
       GREATEST(0, COUNT(p.passenger_id) - f.capacity) AS waitlist_cnt 
  FROM Flights f 
       LEFT JOIN Passengers p ON (f.flight_id = p.flight_id)
 GROUP BY f.flight_id, f.capacity
 ORDER BY f.flight_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select f.flight_id,
       least(count(p.passenger_id), f.capacity) as booked_cnt,
       greatest(count(p.passenger_id) - f.capacity, 0) as waitlist_cnt
  from flights f
       left join passengers p on (f.flight_id = p.flight_id)
 group by f.flight_id, f.capacity
 order by f.flight_id
;


-- SQL Server
/* Write your T-SQL query statement below */
SELECT f.flight_id,
       CASE WHEN f.capacity <= COUNT(p.passenger_id) THEN f.capacity ELSE COUNT(p.passenger_id) END AS booked_cnt,
       CASE WHEN COUNT(p.passenger_id) - f.capacity <= 0 THEN 0 ELSE COUNT(p.passenger_id) - f.capacity END AS waitlist_cnt
       --LEAST(f.capacity, COUNT(p.passenger_id)) AS booked_cnt, 
       --GREATEST(0, COUNT(p.passenger_id) - f.capacity) AS waitlist_cnt 
  FROM Flights f 
       LEFT JOIN Passengers p ON (f.flight_id = p.flight_id)
 GROUP BY f.flight_id, f.capacity
 ORDER BY f.flight_id
;


# MySQL
# Write your MySQL query statement below
SELECT f.flight_id, 
       LEAST(f.capacity, COUNT(p.passenger_id)) AS booked_cnt, 
       GREATEST(0, COUNT(p.passenger_id) - f.capacity) AS waitlist_cnt 
  FROM Flights f 
       LEFT JOIN Passengers p ON f.flight_id = p.flight_id 
 GROUP BY f.flight_id 
 ORDER BY f.flight_id
;


# Pandas
import pandas as pd

def waitlist_analysis(flights: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    df = ( passengers
          .groupby('flight_id', as_index=False)['passenger_id']
          .count()
          .rename(columns={'passenger_id':'total_booked'})
         )
    df1 = flights.merge(df, how='left', on='flight_id').fillna(0)
    df1['booked_cnt'] = df1.apply(lambda row: min(row['total_booked'], row['capacity']), axis=1)
    df1['waitlist_cnt'] = np.where(df1['total_booked'] - df1['capacity'] >= 0, df1['total_booked'] - df1['capacity'], 0)
    return df1[['flight_id', 'booked_cnt', 'waitlist_cnt']].sort_values('flight_id')

