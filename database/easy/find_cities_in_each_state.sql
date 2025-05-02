-- Oracle


-- PostgreSQL


-- SQL Server
/* Write your T-SQL query statement below */
select state, string_agg(city, ', ') within group (order by city) as cities
from cities
group by state
order by state
;


# MySQL


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
