-- Oracle
/* Write your PL/SQL query statement below */
with t (city_id, day, degree, max_temperature) as (
select city_id, day, degree,
       max(degree) over (partition by city_id) as max_temperature
from weather
),
t1 (city_id, day, degree, max_temperature, rnum) as (
select city_id, day, degree, max_temperature,
       row_number() over (partition by city_id order by day) as rnum
from t
where degree = max_temperature
)
select city_id, to_char(day, 'YYYY-MM-DD') as day, degree
from t1
where rnum = 1
order by city_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (city_id, day, degree, max_temperature) as (
select city_id, day, degree,
       max(degree) over (partition by city_id) as max_temperature
from weather
),
t1 (city_id, day, degree, max_temperature, rnum) as (
select city_id, day, degree, max_temperature,
       row_number() over (partition by city_id order by day) as rnum
from t
where degree = max_temperature
)
select city_id, day, degree
from t1
where rnum = 1
order by city_id
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (city_id, day, degree, max_temperature) as (
select city_id, day, degree,
       max(degree) over (partition by city_id) as max_temperature
from weather
),
t1 (city_id, day, degree, max_temperature, rnum) as (
select city_id, day, degree, max_temperature,
       row_number() over (partition by city_id order by day) as rnum
from t
where degree = max_temperature
)
select city_id, day, degree
from t1
where rnum = 1
order by city_id
;


# MySQL
# Write your MySQL query statement below
with t (city_id, day, degree, max_temperature) as (
select city_id, day, degree,
       max(degree) over (partition by city_id) as max_temperature
from weather
),
t1 (city_id, day, degree, max_temperature, rnum) as (
select city_id, day, degree, max_temperature,
       row_number() over (partition by city_id order by day) as rnum
from t
where degree = max_temperature
)
select city_id, day, degree
from t1
where rnum = 1
order by city_id
;


# Pandas
import pandas as pd

def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:
    df = ( weather
          .assign(drnk=weather.groupby('city_id', as_index=False)['degree'].rank(method='dense', ascending=False))
          .query('drnk==1')
         )
    return ( df
            .assign(rnk=df.groupby('city_id', as_index=False)['day'].rank(method='min'))
            .query('rnk==1')[['city_id','day','degree']]
            .sort_values('city_id')
           )

