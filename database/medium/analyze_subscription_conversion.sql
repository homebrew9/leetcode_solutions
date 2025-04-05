-- Oracle
/* Write your PL/SQL query statement below */
-- Solution 1
with t as (
    select user_id, activity_type, round(avg(activity_duration), 2) as avg_duration
      from UserActivity
     group by user_id, activity_type
)
select user_id,
       max(case when activity_type = 'free_trial' then avg_duration end) as trial_avg_duration,
       max(case when activity_type = 'paid' then avg_duration end) as paid_avg_duration
  from t
 group by user_id
 having max(case when activity_type = 'paid' then avg_duration end) is not null
 order by user_id
;

-- Solution 2
/* Write your PL/SQL query statement below */
with t_free as (
    select user_id, round(avg(activity_duration), 2) as trial_avg_duration
      from UserActivity
     where activity_type = 'free_trial'
     group by user_id
),
t_paid as (
    select user_id, round(avg(activity_duration), 2) as paid_avg_duration
      from UserActivity
     where activity_type = 'paid'
     group by user_id
)
select tf.user_id, tf.trial_avg_duration, tp.paid_avg_duration
  from t_free tf
       inner join t_paid tp on (tp.user_id = tf.user_id)
 order by tf.user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- Solution 1
-- Write your PostgreSQL query statement below
with t as (
    select user_id, activity_type, round(avg(activity_duration), 2) as avg_duration
      from UserActivity
     group by user_id, activity_type
)
select user_id,
       max(case when activity_type = 'free_trial' then avg_duration end) as trial_avg_duration,
       max(case when activity_type = 'paid' then avg_duration end) as paid_avg_duration
  from t
 group by user_id
 having max(case when activity_type = 'paid' then avg_duration end) is not null
 order by user_id
;

-- Solution 2
with t_free as (
    select user_id, round(avg(activity_duration), 2) as trial_avg_duration
      from UserActivity
     where activity_type = 'free_trial'
     group by user_id
),
t_paid as (
    select user_id, round(avg(activity_duration), 2) as paid_avg_duration
      from UserActivity
     where activity_type = 'paid'
     group by user_id
)
select tf.user_id, tf.trial_avg_duration, tp.paid_avg_duration
  from t_free tf
       inner join t_paid tp on (tp.user_id = tf.user_id)
 order by tf.user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select user_id, activity_type, round(avg(convert(float, activity_duration)), 2) as avg_duration
      from UserActivity
     group by user_id, activity_type
)
select user_id,
       max(case when activity_type = 'free_trial' then avg_duration end) as trial_avg_duration,
       max(case when activity_type = 'paid' then avg_duration end) as paid_avg_duration
  from t
 group by user_id
 having max(case when activity_type = 'paid' then avg_duration end) is not null
 order by user_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select user_id, activity_type, round(avg(activity_duration), 2) as avg_duration
      from UserActivity
     group by user_id, activity_type
)
select user_id,
       max(case when activity_type = 'free_trial' then avg_duration end) as trial_avg_duration,
       max(case when activity_type = 'paid' then avg_duration end) as paid_avg_duration
  from t
 group by user_id
 having max(case when activity_type = 'paid' then avg_duration end) is not null
 order by user_id
;


# Pandas
import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    df = user_activity.groupby(['user_id','activity_type'], as_index=0)['activity_duration'].mean()
    # Python implements Banker''s rounding which rounds to the nearest even number.
    # round(2.5) = 2 and round(3.5) = 4. In this problem, if the average is 70.625 then
    # round(70.625, 2) returns 70.62, but we want 70.63 i.e. rounded up value. Hence the customized
    # lambda function has been used.
    #df['activity_duration'] = round(df['activity_duration'], 2)
    df['activity_duration'] = df['activity_duration'].apply(lambda x: np.floor(x * 100 + 0.5)/100)
    return ( df[df['activity_type']=='free_trial']
            .merge(
                     df[df['activity_type'] == 'paid'], how='inner', on='user_id'
                  )[['user_id','activity_duration_x','activity_duration_y']]
            .rename(columns={'activity_duration_x': 'trial_avg_duration', 'activity_duration_y': 'paid_avg_duration'})
            .sort_values('user_id')
           )

