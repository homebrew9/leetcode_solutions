-- Oracle
/* Write your PL/SQL query statement below */
with t_start as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'start'
),
t_stop as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'stop'
),
t as (
    select x.server_id, x.status_time, y.status_time, y.status_time - x.status_time as diff
      from t_start x
           inner join t_stop y on (y.server_id = x.server_id and y.rn = x.rn)
)
select floor(sum(diff)) as total_uptime_days
  from t
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t_start as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'start'
),
t_stop as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'stop'
),
t as (
    select x.server_id, x.status_time, y.status_time,
           extract(epoch from y.status_time - x.status_time) as diff
      from t_start x
           inner join t_stop y on (y.server_id = x.server_id and y.rn = x.rn)
)
select floor(sum(diff::numeric/60/60/24)) as total_uptime_days
  from t
;


-- SQL Server
/* Write your T-SQL query statement below */
with t_start as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'start'
),
t_stop as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'stop'
),
t as (
    select x.server_id, --x.status_time, y.status_time,
           datediff(second, x.status_time, y.status_time) as diff
      from t_start x
           inner join t_stop y on (y.server_id = x.server_id and y.rn = x.rn)
)
select floor(sum(convert(float, diff)/60/60/24)) as total_uptime_days
  from t
;


# MySQL
# Write your MySQL query statement below
with t_start as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'start'
),
t_stop as (
    select server_id, status_time, session_status,
           row_number() over (partition by server_id order by status_time) as rn
      from servers
     where session_status = 'stop'
),
t as (
    select x.server_id, x.status_time as from_ts, y.status_time as to_ts,
           timestampdiff(second, x.status_time, y.status_time) as diff
      from t_start x
           inner join t_stop y on (y.server_id = x.server_id and y.rn = x.rn)
)
select floor(sum(diff/60/60/24)) as total_uptime_days
  from t
;


# Pandas
import pandas as pd

def server_utilization_time(servers: pd.DataFrame) -> pd.DataFrame:
    df_start = servers[servers['session_status']=='start'].sort_values(by=['server_id','status_time'])
    df_start['rn'] = df_start.groupby('server_id',as_index=0)['status_time'].rank(method='dense')
    
    df_stop = servers[servers['session_status']=='stop'].sort_values(by=['server_id','status_time'])
    df_stop['rn'] = df_stop.groupby('server_id',as_index=0)['status_time'].rank(method='dense')
    
    df = df_start.merge(df_stop, how='inner', on=['server_id', 'rn'])
    
    # Not sure why the next 2 lines are required. Why would 'status_time_x'/'status_time_y' get converted
    # to strings? These 2 lines are not required in Pandas 2.2.1; LC uses Pandas 2.0.2
    df['status_time_y'] = pd.to_datetime(df['status_time_y'])
    df['status_time_x'] = pd.to_datetime(df['status_time_x'])
    
    df['total_uptime_seconds'] = (df['status_time_y'] - df['status_time_x']).dt.total_seconds()
    return pd.DataFrame(data={'total_uptime_days': int(df['total_uptime_seconds'].sum()/60/60/24)}, index=[0])

