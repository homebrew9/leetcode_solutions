-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select employee_id, start_time, end_time,
           row_number() over (partition by employee_id order by start_time) as rnum
      from EmployeeShifts
),
t1 as (
    select t1.employee_id, t1.rnum,
           (t1.end_time - t2.start_time) * 24 * 60 as overlap_minutes
      from t t1
           inner join t t2 on (t2.employee_id = t1.employee_id and
                               t2.rnum > t1.rnum and
                               t2.start_time between t1.start_time and t1.end_time
                              )
),
t2 as (
    select x.employee_id, max(x.overlapping_shifts) + 1 as max_overlapping_shifts
      from (
                select employee_id, rnum, count(*) as overlapping_shifts
                  from t1
                 group by employee_id, rnum
           ) x
     group by x.employee_id
),
t3 as (
    select t1.employee_id, sum(t1.overlap_minutes) as total_overlap_duration
      from t1
     group by t1.employee_id
)
select t2.employee_id, t2.max_overlapping_shifts, t3.total_overlap_duration
  from t2
       inner join t3 on (t3.employee_id = t2.employee_id)
union all
select distinct es.employee_id, 1 as max_overlapping_shifts, 0 as total_overlap_duration
  from EmployeeShifts es
 where es.employee_id not in (select employee_id from t1)
order by employee_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select employee_id, start_time, end_time,
           row_number() over (partition by employee_id order by start_time) as rnum
      from EmployeeShifts
),
t1 as (
    select t1.employee_id, t1.rnum,
           extract(epoch from t1.end_time - t2.start_time)/60 as overlap_minutes
      from t t1
           inner join t t2 on (t2.employee_id = t1.employee_id and
                               t2.rnum > t1.rnum and
                               t2.start_time between t1.start_time and t1.end_time
                              )
),
t2 as (
    select x.employee_id, max(x.overlapping_shifts) + 1 as max_overlapping_shifts
      from (
                select employee_id, rnum, count(*) as overlapping_shifts
                  from t1
                 group by employee_id, rnum
           ) x
     group by x.employee_id
),
t3 as (
    select t1.employee_id, sum(t1.overlap_minutes) as total_overlap_duration
      from t1
     group by t1.employee_id
)
select t2.employee_id, t2.max_overlapping_shifts, t3.total_overlap_duration
  from t2
       inner join t3 on (t3.employee_id = t2.employee_id)
union all
select distinct es.employee_id, 1 as max_overlapping_shifts, 0 as total_overlap_duration
  from EmployeeShifts es
 where es.employee_id not in (select employee_id from t1)
order by employee_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select employee_id, start_time, end_time,
           row_number() over (partition by employee_id order by start_time) as rnum
      from EmployeeShifts
),
t1 as (
    select t1.employee_id, t1.rnum,
           DATEDIFF(MINUTE, t2.start_time, t1.end_time) as overlap_minutes
      from t t1
           inner join t t2 on (t2.employee_id = t1.employee_id and
                               t2.rnum > t1.rnum and
                               t2.start_time between t1.start_time and t1.end_time
                              )
),
t2 as (
    select x.employee_id, max(x.overlapping_shifts) + 1 as max_overlapping_shifts
      from (
                select employee_id, rnum, count(*) as overlapping_shifts
                  from t1
                 group by employee_id, rnum
           ) x
     group by x.employee_id
),
t3 as (
    select t1.employee_id, sum(t1.overlap_minutes) as total_overlap_duration
      from t1
     group by t1.employee_id
)
select t2.employee_id, t2.max_overlapping_shifts, t3.total_overlap_duration
  from t2
       inner join t3 on (t3.employee_id = t2.employee_id)
union all
select distinct es.employee_id, 1 as max_overlapping_shifts, 0 as total_overlap_duration
  from EmployeeShifts es
 where es.employee_id not in (select employee_id from t1)
order by employee_id
;


# MySQL
# Write your MySQL query statement below
with t as (
    select employee_id, start_time, end_time,
           row_number() over (partition by employee_id order by start_time) as rnum
      from EmployeeShifts
),
t1 as (
    select t1.employee_id, t1.rnum,
           TIMESTAMPDIFF(MINUTE, t2.start_time, t1.end_time) as overlap_minutes
      from t t1
           inner join t t2 on (t2.employee_id = t1.employee_id and
                               t2.rnum > t1.rnum and
                               t2.start_time between t1.start_time and t1.end_time
                              )
),
t2 as (
    select x.employee_id, max(x.overlapping_shifts) + 1 as max_overlapping_shifts
      from (
                select employee_id, rnum, count(*) as overlapping_shifts
                  from t1
                 group by employee_id, rnum
           ) x
     group by x.employee_id
),
t3 as (
    select t1.employee_id, sum(t1.overlap_minutes) as total_overlap_duration
      from t1
     group by t1.employee_id
)
select t2.employee_id, t2.max_overlapping_shifts, t3.total_overlap_duration
  from t2
       inner join t3 on (t3.employee_id = t2.employee_id)
union all
select distinct es.employee_id, 1 as max_overlapping_shifts, 0 as total_overlap_duration
  from EmployeeShifts es
 where es.employee_id not in (select employee_id from t1)
order by employee_id
;


# Pandas
import pandas as pd

def calculate_shift_overlaps(employee_shifts: pd.DataFrame) -> pd.DataFrame:
    employee_shifts['start_time'] = pd.to_datetime(employee_shifts['start_time'])
    employee_shifts['end_time'] = pd.to_datetime(employee_shifts['end_time'])
    df = ( employee_shifts
          .merge(employee_shifts, how='inner', on='employee_id')
          .query('start_time_x < start_time_y <= end_time_x')
         )
    df['overlapping_minutes'] = (df['end_time_x'] - df['start_time_y'])/pd.Timedelta(minutes=1)
    df1 = ( df
           .groupby(['employee_id','start_time_x'], as_index=0)['start_time_y']
           .count()
           .groupby('employee_id', as_index=0)['start_time_y']
           .max()
           .rename(columns={'start_time_y':'max_overlapping_shifts'})
          )
    df1['max_overlapping_shifts'] = df1['max_overlapping_shifts'] + 1
    df2 = ( df
           .groupby('employee_id', as_index=0)['overlapping_minutes']
           .sum()
           .rename(columns={'overlapping_minutes':'total_overlap_duration'})
          )
    df3 = ( employee_shifts[~employee_shifts['employee_id'].isin(df['employee_id'])][['employee_id']]
           .drop_duplicates()
          )
    df3 = df3.assign(max_overlapping_shifts=1, total_overlap_duration=0)
    return ( pd.concat(
                         [df1.merge(df2, how='inner', on='employee_id'), df3]
                      )
            .sort_values('employee_id')
           )

