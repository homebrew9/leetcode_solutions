-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select log_id, case lag(log_id) over (order by log_id) when log_id -1 then 0 else 1 end as marker
      from logs
),
t1 as (
    select log_id, marker, sum(marker) over (order by log_id) as group_id
      from t
)
select min(log_id) as start_id, max(log_id) as end_id
  from t1
 group by group_id
 order by start_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (log_id, group_id) as (
select log_id, log_id - row_number() over (order by log_id) as group_id
from logs
)
select min(log_id) as start_id, max(log_id) as end_id
from t
group by group_id
order by group_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (log_id, group_id) as (
select log_id, log_id - row_number() over (order by log_id) as group_id
from logs
)
select min(log_id) as start_id, max(log_id) as end_id
from t
group by group_id
order by group_id
;


# MySQL
# Write your MySQL query statement below
with t (log_id, group_id) as (
select log_id, log_id - row_number() over (order by log_id) as group_id
from logs
)
select min(log_id) as start_id, max(log_id) as end_id
from t
group by group_id
order by group_id
;


# Pandas
import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:
    logs['group_id'] = logs['log_id'] - logs.index
    return (  pd.merge(
                  logs.groupby('group_id',as_index=False)['log_id'].min(),
                  logs.groupby('group_id',as_index=False)['log_id'].max(),
                  how='inner',
                  on='group_id'
              )[['log_id_x','log_id_y']]
               .rename(columns={'log_id_x':'start_id','log_id_y':'end_id'})
           )

