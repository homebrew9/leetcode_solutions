-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select case when from_id < to_id then from_id else to_id end as person1,
           case when from_id > to_id then from_id else to_id end as person2,
           duration
      from calls
)
select person1, person2, count(*) as call_count, sum(duration) as total_duration
  from t
 group by person1, person2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select case when from_id < to_id then from_id else to_id end as person1,
       case when from_id > to_id then from_id else to_id end as person2,
       count(*) as call_count,
       sum(duration) as total_duration
from calls
group by case when from_id < to_id then from_id else to_id end,
         case when from_id > to_id then from_id else to_id end
;


-- SQL Server
/* Write your T-SQL query statement below */
select case when from_id < to_id then from_id else to_id end as person1,
       case when from_id > to_id then from_id else to_id end as person2,
       count(*) as call_count,
       sum(duration) as total_duration
from calls
group by case when from_id < to_id then from_id else to_id end,
         case when from_id > to_id then from_id else to_id end
;


# MySQL
# Write your MySQL query statement below
select least(from_id, to_id) as person1,
       greatest(from_id, to_id) as person2,
       count(*) as call_count,
       sum(duration) as total_duration
from calls
group by least(from_id, to_id),
         greatest(from_id, to_id)
;


# Pandas
import pandas as pd

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    calls = (  calls.assign(
                 person1 = np.where(calls['from_id'] < calls['to_id'], calls['from_id'], calls['to_id']),
                 person2 = np.where(calls['from_id'] > calls['to_id'], calls['from_id'], calls['to_id']),
                 call_count = 1
               )
            )
    return (  calls.groupby(['person1','person2'],as_index=False)
                   .agg({'call_count': 'sum', 'duration': 'sum'})
                   .rename(columns={'duration':'total_duration'})
           )

