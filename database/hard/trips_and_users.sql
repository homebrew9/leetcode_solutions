-- Oracle
/* Write your PL/SQL query statement below */
-- My guess is that TRIPS.REQUEST_AT is a string instead of a date in Oracle. Both of the following
-- expressions: DATE'2013-10-01' and TO_DATE('2013-10-01','YYYY-MM-DD') throw the following error:
-- "ORA-01861: literal does not match format string"
with t as (
select t.request_at,
       sum(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1 else 0 end) as canceled_trips,
       count(*) as total_trips
from trips t
     inner join users u1 on (u1.users_id = t.client_id and u1.banned = 'No')
     inner join users u2 on (u2.users_id = t.driver_id and u2.banned = 'No')
where t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at
)
select request_at as "Day",
       round(canceled_trips / total_trips, 2) as "Cancellation Rate"
from t
order by 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
select t.request_at,
       sum(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1 else 0 end) as canceled_trips,
       count(*) as total_trips
from trips t
     inner join users u1 on (u1.users_id = t.client_id and u1.banned = 'No')
     inner join users u2 on (u2.users_id = t.driver_id and u2.banned = 'No')
where t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at
)
select request_at as "Day",
       round(canceled_trips::numeric / total_trips::numeric, 2) as "Cancellation Rate"
from t
order by 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
select t.request_at,
       sum(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1 else 0 end) as canceled_trips,
       count(*) as total_trips
from trips t
     inner join users u1 on (u1.users_id = t.client_id and u1.banned = 'No')
     inner join users u2 on (u2.users_id = t.driver_id and u2.banned = 'No')
where t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at
)
select request_at as "Day",
       round(CONVERT(FLOAT, canceled_trips) / CONVERT(FLOAT, total_trips), 2) as "Cancellation Rate"
from t
order by 1
;


# MySQL
# Write your MySQL query statement below
with t as (
select t.request_at,
       sum(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1 else 0 end) as canceled_trips,
       count(*) as total_trips
from trips t
     inner join users u1 on (u1.users_id = t.client_id and u1.banned = 'No')
     inner join users u2 on (u2.users_id = t.driver_id and u2.banned = 'No')
where t.request_at between '2013-10-01' and '2013-10-03'
group by t.request_at
)
select request_at as "Day",
       round(canceled_trips / total_trips, 2) as "Cancellation Rate"
from t
order by 1
;


# Pandas
import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # For some reason, the column trips.request_at is a string, and not a date. Hence, simple string comparison works.
    # Otherwise, we need to convert to date explicitly and then use .dt accessor as seen below.
    # ===============
    #trips.request_at = pd.to_datetime(trips.request_at)
    #mask = ( (trips['request_at'].dt.strftime('%Y-%m-%d') >= '2013-10-01')
    #         &
    #         (trips['request_at'].dt.strftime('%Y-%m-%d') <= '2013-10-03')
    #       )
    #trips = trips[mask]
    # ===============
    mask = (trips['request_at'] >= '2013-10-01') & (trips['request_at'] <= '2013-10-03')
    trips = trips[mask]
    users = users[users['banned'] == 'No']
    df = ( trips[mask]
          .merge(users, how='inner', left_on='client_id', right_on='users_id')
          .merge(users, how='inner', left_on='driver_id', right_on='users_id')[['request_at','status','id']]
         )
    df['status_cd'] = np.where((df['status']=='cancelled_by_client')|(df['status']=='cancelled_by_driver'), 1, 0)
    df = ( df
          .groupby('request_at', as_index=False)
          .agg(cancelled=('status_cd','sum'), total=('id','count'))
         )
    df['Cancellation Rate'] = round(df['cancelled']/df['total'], 2)
    return df[['request_at','Cancellation Rate']].rename(columns={'request_at': 'Day'})

