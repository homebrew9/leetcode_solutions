-- Oracle
/* Write your PL/SQL query statement below */
select c.country_name,
       case when avg(weather_state) <= 15 then 'Cold'
            when avg(weather_state) >= 25 then 'Hot'
            else 'Warm'
        end as weather_type
from countries c
     inner join weather w on (w.country_id = c.country_id)
where trunc(w.day, 'month') = date'2019-11-01'
group by c.country_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select c.country_name,
       case when avg(weather_state) <= 15 then 'Cold'
            when avg(weather_state) >= 25 then 'Hot'
            else 'Warm'
        end as weather_type
from countries c
     inner join weather w on (w.country_id = c.country_id)
where date_trunc('month', w.day) = DATE'2019-11-01'
group by c.country_name
;


-- SQL Server
/* Write your T-SQL query statement below */
select c.country_name,
       case when convert(float, sum(weather_state))/convert(float, count(*)) <= 15 then 'Cold'
            when convert(float, sum(weather_state))/convert(float, count(*)) >= 25 then 'Hot'
            else 'Warm'
        end as weather_type
from countries c
     inner join weather w on (w.country_id = c.country_id)
where year(w.day) = 2019
and month(w.day) = 11
group by c.country_name
;


# MySQL
# Write your MySQL query statement below
select c.country_name,
       case when avg(weather_state) <= 15 then 'Cold'
            when avg(weather_state) >= 25 then 'Hot'
            else 'Warm'
        end as weather_type
from countries c
     inner join weather w on (w.country_id = c.country_id)
where year(w.day) = 2019
and month(w.day) = 11
group by c.country_name
;


# Pandas
import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    df = countries.merge(weather, how='inner', on='country_id')
    df1 = ( df[(df['day']>='2019-11-01') & (df['day']<='2019-11-30')]
            .groupby('country_name', as_index=False)['weather_state']
            .mean()
          )
    df1['weather_type'] = np.where( df1['weather_state'] <= 15, 'Cold',
                                        np.where(df1['weather_state'] >= 25, 'Hot', 'Warm')
                                  )
    return df1[['country_name', 'weather_type']]

