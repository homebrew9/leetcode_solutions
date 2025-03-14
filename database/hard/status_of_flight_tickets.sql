-- Oracle
/* Write your PL/SQL query statement below */
with t (passenger_id, flight_id, booking_time, rnk, capacity) as (
select p.passenger_id, p.flight_id, p.booking_time,
       rank() over (partition by p.flight_id order by p.booking_time) as rnk,
       f.capacity
from passengers p
     inner join flights f on (f.flight_id = p.flight_id)
)
select passenger_id,
       case when rnk <= capacity then 'Confirmed' else 'Waitlist' end as status
from t
order by passenger_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (passenger_id, flight_id, booking_time, rnk, capacity) as (
select p.passenger_id, p.flight_id, p.booking_time,
       rank() over (partition by p.flight_id order by p.booking_time) as rnk,
       f.capacity
from passengers p
     inner join flights f on (f.flight_id = p.flight_id)
)
select passenger_id,
       case when rnk <= capacity then 'Confirmed' else 'Waitlist' end as status
from t
order by passenger_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (passenger_id, flight_id, booking_time, rnk, capacity) as (
select p.passenger_id, p.flight_id, p.booking_time,
       rank() over (partition by p.flight_id order by p.booking_time) as rnk,
       f.capacity
from passengers p
     inner join flights f on (f.flight_id = p.flight_id)
)
select passenger_id,
       case when rnk <= capacity then 'Confirmed' else 'Waitlist' end as status
from t
order by passenger_id
;


# MySQL
# Write your MySQL query statement below
with t (passenger_id, flight_id, booking_time, rnk, capacity) as (
select p.passenger_id, p.flight_id, p.booking_time,
       rank() over (partition by p.flight_id order by p.booking_time) as rnk,
       f.capacity
from passengers p
     inner join flights f on (f.flight_id = p.flight_id)
)
select passenger_id,
       case when rnk <= capacity then 'Confirmed' else 'Waitlist' end as status
from t
order by passenger_id
;


# Pandas
import pandas as pd

def ticket_status(flights: pd.DataFrame, passengers: pd.DataFrame) -> pd.DataFrame:
    passengers['rnk'] = passengers.groupby('flight_id')['booking_time'].rank(method='min')
    df = passengers.merge(flights, how='inner', on='flight_id')
    df['status'] = np.where(df['rnk'] <= df['capacity'], 'Confirmed', 'Waitlist')
    return df[['passenger_id','status']].sort_values('passenger_id')

