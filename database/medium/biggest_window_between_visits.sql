-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select user_id, visit_date
      from UserVisits
    union all
    select distinct user_id, '2021-01-01' as visit_date
      from UserVisits
),
t1 as (
    select user_id,
           datediff(day, lag(visit_date) over (partition by user_id order by visit_date), visit_date) as visit_window
      from t
)
select user_id, max(visit_window) as biggest_window
  from t1
 group by user_id
 order by user_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select user_id, visit_date
      from UserVisits
    union all
    select distinct user_id, '2021-01-01' as visit_date
      from UserVisits
),
t1 as (
    select user_id,
           timestampdiff(day, lag(visit_date) over (partition by user_id order by visit_date), visit_date) as visit_window
      from t
)
select user_id, max(visit_window) as biggest_window
  from t1
 group by user_id
 order by user_id
;


# Pandas
import pandas as pd

def biggest_window(user_visits: pd.DataFrame) -> pd.DataFrame:
    df = ( pd
          .concat([user_visits,
                   user_visits[['user_id']].drop_duplicates().assign(visit_date=pd.to_datetime('2021-01-01'))
                  ]
                 )
          .sort_values(['user_id','visit_date'])
          .reset_index(drop=True)
         )
    df['prev_user_id'] = df[['user_id']].shift(1)
    df['prev_visit_date'] = df[['visit_date']].shift(1)
    df['biggest_window'] = ( np.where((~df['prev_user_id'].isna()) & (df['user_id'] == df['prev_user_id']),
                                      (df['visit_date'] - df['prev_visit_date']).dt.days, 0
                                     )
                           )
    return df.groupby('user_id', as_index=0)['biggest_window'].max().sort_values('user_id')

