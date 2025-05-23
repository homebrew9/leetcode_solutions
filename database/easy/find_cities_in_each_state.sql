-- Oracle
/* Write your PL/SQL query statement below */
select state, listagg(city, ', ') within group (order by null) as cities
from cities
group by state
order by state
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select state, string_agg(city, ', ' order by city) as cities
from cities
group by state
order by state
;


-- SQL Server
/* Write your T-SQL query statement below */
select state, string_agg(city, ', ') within group (order by city) as cities
from cities
group by state
order by state
;


# MySQL
# Write your MySQL query statement below
select state, group_concat(city order by city separator ', ') as cities
from cities
group by state
order by state
;


# Pandas
import pandas as pd
from operator import concat
from functools import reduce

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    cities = cities.sort_values(['state','city'])
    cities['city'] = ', ' + cities['city']
    df = ( cities
          .groupby('state', as_index=0)['city']
          .apply(lambda x: reduce(concat, x))
          .rename(columns={'city': 'cities'})
         )
    df['cities'] = df['cities'].str.extract('^, (.*)')
    return df

