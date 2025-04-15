-- Oracle


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select id, recordDate, temperature,
           case
                when recordDate = lag(recordDate) over (order by recordDate) + 1 and
                     temperature > lag(temperature) over (order by recordDate)
                then 'Y'
           end as is_higher
      from weather
)
select id
  from t
 where is_higher = 'Y'
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select id, recordDate, temperature,
           case
                when recordDate = DATEADD(DAY, 1, lag(recordDate) over (order by recordDate)) and
                     temperature > lag(temperature) over (order by recordDate)
                then 'Y'
           end as is_higher
      from weather
)
select id
  from t
 where is_higher = 'Y'
;


# MySQL
# Write your MySQL query statement below
with t as (
    select id, recordDate, temperature,
           case
                when recordDate = DATE_ADD(lag(recordDate) over (order by recordDate), INTERVAL 1 DAY) and
                     temperature > lag(temperature) over (order by recordDate)
                then 'Y'
           end as is_higher
      from weather
)
select id
  from t
 where is_higher = 'Y'
;


# Pandas
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)
    weather['prev_date'] = weather.shift(1)['recordDate']
    weather['prev_temp'] = weather.shift(1)['temperature']
    weather['is_higher'] = ( np.where(
                               ((weather['recordDate'] - weather['prev_date'])/np.timedelta64(1,'D') == 1)
                               &
                               (weather['temperature'] > weather['prev_temp']), 'Y', 'N'
                             )
                           )
    return weather[weather['is_higher'] == 'Y'][['id']]

