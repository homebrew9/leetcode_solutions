-- Oracle
/* Write your PL/SQL query statement below */
-- Old-style
select s1.user_id, to_char(s1.steps_date, 'YYYY-MM-DD') as steps_date,
       round((s1.steps_count+s2.steps_count+s3.steps_count)/3, 2) as rolling_average
from steps s1
     inner join steps s2 on (s2.user_id = s1.user_id and s2.steps_date = s1.steps_date - 1)
     inner join steps s3 on (s3.user_id = s2.user_id and s3.steps_date = s2.steps_date - 1)
order by s1.user_id, s1.steps_date
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- Old-style
select s1.user_id, s1.steps_date,
       round((s1.steps_count+s2.steps_count+s3.steps_count)::numeric/3::numeric, 2) as rolling_average
from steps s1
     inner join steps s2 on (s2.user_id = s1.user_id and s2.steps_date = s1.steps_date - 1)
     inner join steps s3 on (s3.user_id = s2.user_id and s3.steps_date = s2.steps_date - 1)
order by s1.user_id, s1.steps_date
;


-- SQL Server
/* Write your T-SQL query statement below */
-- Old-style
select s1.user_id, s1.steps_date,
       round(CONVERT(FLOAT, (s1.steps_count+s2.steps_count+s3.steps_count)) / 3.0, 2) as rolling_average
from steps s1
     inner join steps s2 on (s2.user_id = s1.user_id and s2.steps_date = DATEADD(DAY, -1, s1.steps_date))
     inner join steps s3 on (s3.user_id = s2.user_id and s3.steps_date = DATEADD(DAY, -1, s2.steps_date))
order by s1.user_id, s1.steps_date
;


# MySQL
# Write your MySQL query statement below
-- Old-style
select s1.user_id, s1.steps_date,
       round((s1.steps_count+s2.steps_count+s3.steps_count)/3, 2) as rolling_average
from steps s1
     inner join steps s2 on (s2.user_id = s1.user_id and s2.steps_date = DATE_SUB(s1.steps_date, INTERVAL 1 DAY))
     inner join steps s3 on (s3.user_id = s2.user_id and s3.steps_date = DATE_SUB(s2.steps_date, INTERVAL 1 DAY))
order by s1.user_id, s1.steps_date
;


# Pandas
import pandas as pd

def rolling_average(steps: pd.DataFrame) -> pd.DataFrame:
    df1 = steps.sort_values(['user_id','steps_date']).shift(1)
    df2 = steps.sort_values(['user_id','steps_date']).shift(2)
    steps['1_day_prior'] = steps['steps_date'] - pd.Timedelta(1,'D')
    steps['2_day_prior'] = steps['steps_date'] - pd.Timedelta(2,'D')
    df = ( steps
          .merge(df1, how='inner', left_on=['user_id','1_day_prior'], right_on=['user_id','steps_date'])
          .merge(df2, how='inner', left_on=['user_id','2_day_prior'], right_on=['user_id','steps_date'])
         )
    df['rolling_average'] = round((df['steps_count_x']+df['steps_count_y']+df['steps_count'])/3, 2)
    return ( df[['user_id','steps_date_x','rolling_average']]
            .rename(columns={'steps_date_x':'steps_date'})
            .sort_values(['user_id','steps_date'])
           )

