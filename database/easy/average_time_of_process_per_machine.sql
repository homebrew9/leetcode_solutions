-- Oracle
/* Write your PL/SQL query statement below */
with t (machine_id, process_id, start_ts, end_ts) as (
    select machine_id, process_id,
           max(decode(activity_type, 'start', timestamp)) as start_ts,
           max(decode(activity_type, 'end', timestamp)) as end_ts
      from Activity
     group by machine_id, process_id
)
select machine_id, round(avg(end_ts - start_ts), 3) as processing_time
from t
group by machine_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select a1.machine_id,
       round(sum(a2.timestamp - a1.timestamp)::numeric / count(a1.process_id)::numeric, 3) as processing_time
  from activity a1
       inner join activity a2
       on (a2.machine_id = a1.machine_id and a2.process_id = a1.process_id and a2.activity_type = 'end')
 where a1.activity_type = 'start'
 group by a1.machine_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select a1.machine_id,
       round(convert(float, sum(a2.timestamp - a1.timestamp)) / convert(float, count(a1.process_id)), 3) as processing_time
  from activity a1
       inner join activity a2
       on (a2.machine_id = a1.machine_id and a2.process_id = a1.process_id and a2.activity_type = 'end')
 where a1.activity_type = 'start'
 group by a1.machine_id
;


# MySQL
# Write your MySQL query statement below
select a1.machine_id,
       round(sum(a2.timestamp - a1.timestamp) / count(a1.process_id), 3) as processing_time
  from activity a1
       inner join activity a2
       on (a2.machine_id = a1.machine_id and a2.process_id = a1.process_id and a2.activity_type = 'end')
 where a1.activity_type = 'start'
 group by a1.machine_id
;


# Pandas
import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    df_count = ( activity
                .groupby('machine_id', as_index=0)
                .agg(process_count=('process_id', 'nunique'))
               )
    df = ( activity[activity['activity_type']=='start']
          .merge(activity[activity['activity_type']=='end'], how='inner', on=['machine_id','process_id'])
         )
    df['run_time'] = df['timestamp_y'] - df['timestamp_x']
    df1 = ( df
           .groupby('machine_id', as_index=0)
           .agg(total_run_time=('run_time', 'sum'))
           .merge(df_count, how='inner', on='machine_id')
          )
    df1['processing_time'] = round(df1['total_run_time'] / df1['process_count'], 3)
    return df1[['machine_id','processing_time']]


