-- Oracle
/* Write your PL/SQL query statement below */
with t_marker as (
    select t.task_id, t.employee_id, t.start_time, t.end_time,
           case when t.start_time < lag(t.end_time) over (partition by t.employee_id order by t.start_time)
                then 0
                else 1
           end as marker,
           (select count(*) + 1
              from tasks t1
             where t1.employee_id = t.employee_id
               and t1.start_time > t.start_time
               and t1.start_time < t.end_time
           ) as concurrent_tasks
      from tasks t
),
t_max_ct as (
    select tm.employee_id, max(concurrent_tasks) as max_concurrent_tasks
      from t_marker tm
     group by tm.employee_id
),
t_task_hours as (
    select task_id, employee_id, start_time, end_time, marker,
           sum(marker) over (partition by employee_id order by start_time) as group_id
      from t_marker
),
t_task_hours1 as (
    select tth.employee_id, tth.group_id, min(tth.start_time) as start_time, max(tth.end_time) as end_time,
           (max(tth.end_time) - min(tth.start_time)) * 24 as total_hours
      from t_task_hours tth
     group by tth.employee_id, tth.group_id
),
t_total_task_hours as (
    select employee_id, floor(sum(total_hours)) as total_task_hours
      from t_task_hours1
    group by employee_id
)
select ttth.employee_id, ttth.total_task_hours, tmc.max_concurrent_tasks
  from t_total_task_hours ttth
       inner join t_max_ct tmc on (tmc.employee_id = ttth.employee_id)
 order by ttth.employee_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t_marker as (
    select t.task_id, t.employee_id, t.start_time, t.end_time,
           case when t.start_time < lag(t.end_time) over (partition by t.employee_id order by t.start_time)
                then 0
                else 1
           end as marker,
           (select count(*) + 1
              from tasks t1
             where t1.employee_id = t.employee_id
               and t1.start_time > t.start_time
               and t1.start_time < t.end_time
           ) as concurrent_tasks
      from tasks t
),
t_max_ct as (
    select tm.employee_id, max(concurrent_tasks) as max_concurrent_tasks
      from t_marker tm
     group by tm.employee_id
),
t_task_hours as (
    select task_id, employee_id, start_time, end_time, marker,
           sum(marker) over (partition by employee_id order by start_time) as group_id
      from t_marker
),
t_task_hours1 as (
    select tth.employee_id, tth.group_id, min(tth.start_time) as start_time, max(tth.end_time) as end_time,
           extract(epoch from (max(tth.end_time) - min(tth.start_time))) / 60 / 60 as total_hours
      from t_task_hours tth
     group by tth.employee_id, tth.group_id
),
t_total_task_hours as (
    select employee_id, floor(sum(total_hours)) as total_task_hours
      from t_task_hours1
    group by employee_id
)
select ttth.employee_id, ttth.total_task_hours, tmc.max_concurrent_tasks
  from t_total_task_hours ttth
       inner join t_max_ct tmc on (tmc.employee_id = ttth.employee_id)
 order by ttth.employee_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_marker as (
    select t.task_id, t.employee_id, t.start_time, t.end_time,
           case when t.start_time < lag(t.end_time) over (partition by t.employee_id order by t.start_time)
                then 0
                else 1
           end as marker,
           (select count(*) + 1
              from tasks t1
             where t1.employee_id = t.employee_id
               and t1.start_time > t.start_time
               and t1.start_time < t.end_time
           ) as concurrent_tasks
      from tasks t
),
t_max_ct as (
    select tm.employee_id, max(concurrent_tasks) as max_concurrent_tasks
      from t_marker tm
     group by tm.employee_id
),
t_task_hours as (
    select task_id, employee_id, start_time, end_time, marker,
           sum(marker) over (partition by employee_id order by start_time) as group_id
      from t_marker
),
t_task_hours1 as (
    select tth.employee_id, tth.group_id, min(tth.start_time) as start_time, max(tth.end_time) as end_time,
           DATEDIFF(second, min(tth.start_time), max(tth.end_time)) / 60.0 / 60.0 as total_hours
      from t_task_hours tth
     group by tth.employee_id, tth.group_id
),
t_total_task_hours as (
    select employee_id, floor(sum(total_hours)) as total_task_hours
      from t_task_hours1
    group by employee_id
)
select ttth.employee_id, ttth.total_task_hours, tmc.max_concurrent_tasks
  from t_total_task_hours ttth
       inner join t_max_ct tmc on (tmc.employee_id = ttth.employee_id)
 order by ttth.employee_id
;


# MySQL
# Write your MySQL query statement below
with t_marker as (
    select t.task_id, t.employee_id, t.start_time, t.end_time,
           case when t.start_time < lag(t.end_time) over (partition by t.employee_id order by t.start_time)
                then 0
                else 1
           end as marker,
           (select count(*) + 1
              from tasks t1
             where t1.employee_id = t.employee_id
               and t1.start_time > t.start_time
               and t1.start_time < t.end_time
           ) as concurrent_tasks
      from tasks t
),
t_max_ct as (
    select tm.employee_id, max(concurrent_tasks) as max_concurrent_tasks
      from t_marker tm
     group by tm.employee_id
),
t_task_hours as (
    select task_id, employee_id, start_time, end_time, marker,
           sum(marker) over (partition by employee_id order by start_time) as group_id
      from t_marker
),
t_task_hours1 as (
    select tth.employee_id, tth.group_id, min(tth.start_time) as start_time, max(tth.end_time) as end_time,
           TIMESTAMPDIFF(second, min(tth.start_time), max(tth.end_time)) / 60 / 60 as total_hours
      from t_task_hours tth
     group by tth.employee_id, tth.group_id
),
t_total_task_hours as (
    select employee_id, floor(sum(total_hours)) as total_task_hours
      from t_task_hours1
    group by employee_id
)
select ttth.employee_id, ttth.total_task_hours, tmc.max_concurrent_tasks
  from t_total_task_hours ttth
       inner join t_max_ct tmc on (tmc.employee_id = ttth.employee_id)
 order by ttth.employee_id
;


# Pandas
import pandas as pd

def find_total_duration(tasks: pd.DataFrame) -> pd.DataFrame:
    # First we determine the max concurrent tasks by joining each (employee_id, time_range)
    # with itself and counting the number of records. The max of those counts is the max
    # concurrent tasks.
    df = tasks.merge(tasks, how='inner', on='employee_id')
    df['max_concurrent_tasks'] = np.where(
                                   (df['start_time_y'] > df['start_time_x'])
                                   &
                                   (df['start_time_y'] < df['end_time_x']), 1, 0
                                 )
    df = ( df
          .groupby(['employee_id','start_time_x'],as_index=0)['max_concurrent_tasks']
          .sum()
         )
    df['max_concurrent_tasks'] = df['max_concurrent_tasks']+1
    df = ( df
          .groupby('employee_id',as_index=0)['max_concurrent_tasks']
          .max()
         )
    # For total time spent, we first set a marker to denote a fresh new timeslot of activity.
    # The cumulative sum of markers gives us a "group_id". Each group_id denotes a continuous
    # period of activity, so the diff of max(end_time) and min(start_time) gives us the total
    # hours per group_id. Roll that up for total hours per employee_id.
    tasks['marker'] = np.where(
                        (tasks['employee_id'] == tasks['employee_id'].shift(1)[tasks.index])
                        &
                        (tasks['start_time'] < tasks['end_time'].shift(1)[tasks.index]), 0, 1
                      )
    tasks['group_id'] = tasks['marker'].cumsum()
    df1 = ( tasks
           .groupby(['employee_id','group_id'],as_index=0)
           .agg({'start_time': 'min', 'end_time': 'max'})
          )
    # Finally, merge the total_time dataframe with the max_concurrent_tasks dataframe.
    return ( df1
            .assign(total_task_hours=(df1['end_time'] - df1['start_time'])/pd.Timedelta(hours=1))
            .groupby('employee_id',as_index=0)['total_task_hours']
            .sum()
            .astype(int)
            .merge(df, how='inner', on='employee_id')
            .sort_values('employee_id')
           )

