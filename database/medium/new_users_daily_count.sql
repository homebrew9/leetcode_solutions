-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, activity, activity_date, first_login) as (
    select user_id, activity, activity_date,
           min(activity_date) over (partition by user_id) as first_login
    from (select distinct user_id, activity, activity_date
          from traffic
          where activity='login'
         ) t
),
t1 (user_id, activity, activity_date) as (
    select user_id, activity, activity_date
      from t
     where activity_date = first_login
)
select to_char(activity_date,'YYYY-MM-DD') as login_date, count(*) as user_count
from t1
where activity_date between DATE'2019-06-30' - 90 and DATE'2019-06-30'
group by activity_date
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, activity, activity_date, first_login) as (
    select user_id, activity, activity_date,
           min(activity_date) over (partition by user_id) as first_login
    from (select distinct user_id, activity, activity_date
          from traffic
          where activity='login'
         ) t
),
t1 (user_id, activity, activity_date) as (
    select user_id, activity, activity_date
      from t
     where activity_date = first_login
)
select activity_date as login_date, count(*) as user_count
from t1
where activity_date between '2019-06-30'::date - 90 and '2019-06-30'::date
group by activity_date
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, activity, activity_date, first_login) as (
    select user_id, activity, activity_date,
           min(activity_date) over (partition by user_id) as first_login
    from (select distinct user_id, activity, activity_date
          from traffic
          where activity='login'
         ) t
),
t1 (user_id, activity, activity_date) as (
    select user_id, activity, activity_date
      from t
     where activity_date = first_login
)
select activity_date as login_date, count(*) as user_count
from t1
where activity_date between DATEADD(day,-90,'2019-06-30') and '2019-06-30'
group by activity_date
;


# MySQL
# Write your MySQL query statement below
with t (user_id, activity, activity_date, first_login) as (
    select user_id, activity, activity_date,
           min(activity_date) over (partition by user_id) as first_login
    from (select distinct user_id, activity, activity_date
          from traffic
          where activity='login'
         ) t
),
t1 (user_id, activity, activity_date) as (
    select user_id, activity, activity_date
      from t
     where activity_date = first_login
)
select activity_date as login_date, count(*) as user_count
from t1
where activity_date between date_sub('2019-06-30', interval 90 day) and '2019-06-30'
group by activity_date
;


# Pandas
import pandas as pd

def new_users_daily_count(traffic: pd.DataFrame) -> pd.DataFrame:
    return ( traffic[traffic['activity']=='login']
            .drop_duplicates()
            .groupby('user_id',as_index=False)['activity_date']
            .min()
            .assign(to_date=pd.to_datetime('2019-06-30'),
                    from_date=pd.to_datetime('2019-06-30')-pd.to_timedelta(90,'d')
                   )
            .query('activity_date >= from_date and activity_date <= to_date')
            .groupby('activity_date',as_index=False)['user_id']
            .count()
            .rename(columns={'activity_date':'login_date', 'user_id':'user_count'})
           )

