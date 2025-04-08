-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select state,
           listagg(city, ', ') within group (order by city) as cities,
           count(*) as city_count,
           sum(case when substr(state,1,1) = substr(city,1,1) then 1 end) as matching_letter_count
      from cities
     group by state
)
select state, cities, matching_letter_count
  from t
 where city_count >= 3
   and matching_letter_count >= 1
 order by matching_letter_count desc, state
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select state,
           string_agg(city, ', ' order by city) as cities,
           count(*) as city_count,
           sum(case when substr(state,1,1) = substr(city,1,1) then 1 end) as matching_letter_count
      from cities
     group by state
)
select state, cities, matching_letter_count
  from t
 where city_count >= 3
   and matching_letter_count >= 1
 order by matching_letter_count desc, state
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select state,
           string_agg(city, ', ') within group (order by city) as cities,
           count(*) as city_count,
           sum(case when substring(state,1,1) = substring(city,1,1) then 1 end) as matching_letter_count
      from cities
     group by state
)
select state, cities, matching_letter_count
  from t
 where city_count >= 3
   and matching_letter_count >= 1
 order by matching_letter_count desc, state
;


# MySQL
# Write your MySQL query statement below
with t as (
    select state,
           group_concat(city order by city separator ', ') as cities,
           count(*) as city_count,
           sum(case when substr(state,1,1) = substr(city,1,1) then 1 end) as matching_letter_count
      from cities
     group by state
)
select state, cities, matching_letter_count
  from t
 where city_count >= 3
   and matching_letter_count >= 1
 order by matching_letter_count desc, state
;


# Pandas
import pandas as pd

def state_city_analysis(cities: pd.DataFrame) -> pd.DataFrame:
    cities.sort_values(by=['state','city'], inplace=True)
    df = ( cities
          .groupby('state', as_index=0)['city']
          .agg(', '.join).rename(columns={'city': 'cities'})
         )
    return (cities
            .assign(matching_letter_count = np.where(cities['state'].str[:1] == cities['city'].str[:1],1,0))
            .groupby('state', as_index=0)
            .agg({'city': 'count', 'matching_letter_count': 'sum'})
            .query('city >= 3 and matching_letter_count >= 1')[['state','matching_letter_count']]
            .merge(df, how='inner', on='state')[['state','cities','matching_letter_count']]
            .sort_values(by=['matching_letter_count', 'state'], ascending=[False, True])
           )

