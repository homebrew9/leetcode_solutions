-- Oracle
/* Write your PL/SQL query statement below */
with t (city, calling_hour, number_of_calls) as (
select city,
       to_number(to_char(call_time, 'HH24')) as calling_hour,
       count(*) as number_of_calls
from calls
group by city,
       to_char(call_time, 'HH24')
)
select x.city, x.calling_hour as peak_calling_hour, x.number_of_calls
from t x
where x.number_of_calls = (select max(y.number_of_calls)
                           from t y
                           where y.city = x.city
                          )
order by x.calling_hour desc,
         x.city desc
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (city, calling_hour, number_of_calls) as (
select city,
       to_char(call_time, 'HH24')::int as calling_hour,
       count(*) as number_of_calls
from calls
group by city,
       to_char(call_time, 'HH24')
)
select x.city, x.calling_hour as peak_calling_hour, x.number_of_calls
from t x
where x.number_of_calls = (select max(y.number_of_calls)
                           from t y
                           where y.city = x.city
                          )
order by x.calling_hour desc,
         x.city desc
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select city, datepart(hour, call_time) as hr, count(*) as call_count
      from calls
     group by city, datepart(hour, call_time)
),
t1 as (
    select city, hr, call_count, dense_rank() over (partition by city order by call_count desc) as drnk
    from t
)
select city, hr as peak_calling_hour, call_count as number_of_calls
from t1
where drnk = 1
order by hr desc, city desc
;


# MySQL
# Write your MySQL query statement below
with t as (
    select city, hour(call_time) as hr, count(*) as call_count
      from calls
     group by city, hour(call_time)
),
t1 as (
    select city, hr, call_count, dense_rank() over (partition by city order by call_count desc) as drnk
    from t
)
select city, hr as peak_calling_hour, call_count as number_of_calls
from t1
where drnk = 1
order by hr desc, city desc
;


# Pandas
import pandas as pd

def peak_calling_hours(calls: pd.DataFrame) -> pd.DataFrame:
    calls['hr'] = calls['call_time'].dt.hour
    calls = calls.groupby(['city','hr'])['caller_id'].count().reset_index()
    calls['drnk'] = calls.groupby('city')['caller_id'].rank(method='dense', ascending=False)
    return ( calls[calls['drnk']==1][['city','hr','caller_id']]
            .sort_values(by=['hr','city'], ascending=[0,0])
            .rename(columns={'hr': 'peak_calling_hour', 'caller_id':'number_of_calls'})
           )

