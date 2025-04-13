-- Oracle
/* Write your PL/SQL query statement below */
select to_char(activity_date, 'YYYY-MM-DD') as "day",
       count(distinct user_id) as "active_users"
from activity
where activity_date between DATE'2019-07-27' - 29 and DATE'2019-07-27'
group by to_char(activity_date, 'YYYY-MM-DD')
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select activity_date as day, count(distinct(user_id)) as active_users
  from activity
 where activity_date between '2019-07-27'::date - interval '29 days' and '2019-07-27'::date
 group by activity_date
;


-- SQL Server
/* Write your T-SQL query statement below */
select activity_date as day, count(distinct(user_id)) as active_users
  from activity
 where activity_date between dateadd(day, -29, convert(datetime2, '2019-07-27')) and convert(datetime2, '2019-07-27')
 group by activity_date
;


# MySQL
# Write your MySQL query statement below
select activity_date as day, count(distinct(user_id)) as active_users
  from activity
 where activity_date between cast('2019-07-27' as date) - interval '29' day and cast('2019-07-27' as date)
 group by activity_date
;


# Pandas
import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    start_date = pd.to_datetime('2019-07-27') - pd.Timedelta(days=29)
    end_date = pd.to_datetime('2019-07-27')
    return ( activity[(activity['activity_date'] >= start_date) & (activity['activity_date'] <= end_date)]
            .drop_duplicates(subset=['user_id', 'activity_date'])
            .groupby('activity_date', as_index=0)['user_id']
            .count()
            .rename(columns={'activity_date': 'day', 'user_id': 'active_users'})
           )

