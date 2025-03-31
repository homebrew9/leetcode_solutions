-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


# MySQL
# Write your MySQL query statement below
with t as (
    select ag.age_bucket,
           sum(case when ac.activity_type = 'send' then ac.time_spent else 0 end) as total_time_spent_send,
           sum(case when ac.activity_type = 'open' then ac.time_spent else 0 end) as total_time_spent_open,
           sum(ac.time_spent) as total_time_spent
    from activities ac
         inner join age ag on (ag.user_id = ac.user_id)
    group by ag.age_bucket
)
select age_bucket,
       round(total_time_spent_send / total_time_spent * 100, 2) as send_perc,
       round(total_time_spent_open / total_time_spent * 100, 2) as open_perc
from t
;


# Pandas
import pandas as pd

def snap_analysis(activities: pd.DataFrame, age: pd.DataFrame) -> pd.DataFrame:
    df_total = ( age
                .merge(activities, how='inner', on='user_id')
                .groupby('age_bucket', as_index=0)['time_spent']
                .sum()
               )
    df_send = ( age
               .merge(activities[activities['activity_type'] == 'send'], how='inner', on='user_id')
               .groupby('age_bucket', as_index=0)['time_spent']
               .sum()
              )
    df_open = ( age
               .merge(activities[activities['activity_type'] == 'open'], how='inner', on='user_id')
               .groupby('age_bucket', as_index=0)['time_spent']
               .sum()
              )
    df = ( df_total
          .merge(df_send,how='left',on='age_bucket')
          .merge(df_open,how='left',on='age_bucket')
          .fillna(0)
         )
    df['send_perc'] = round(df['time_spent_y'] / df['time_spent_x'] * 100, 2)
    df['open_perc'] = round(df['time_spent'] / df['time_spent_x'] * 100, 2)
    return df[['age_bucket','send_perc','open_perc']]

