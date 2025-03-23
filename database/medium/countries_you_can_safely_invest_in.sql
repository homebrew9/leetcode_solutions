-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (substr(p.phone_number,1,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (substr(p.phone_number,1,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (left(p.phone_number,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


# MySQL
# Write your MySQL query statement below
with t as (
    select caller_id as person_id, duration from calls
    union all
    select callee_id as person_id, duration from calls
)
select c.name as country
  from t
       inner join person p on (p.id = t.person_id)
       inner join country c on (substr(p.phone_number,1,3) = c.country_code)
 group by c.name
having avg(t.duration) > (select avg(duration) from calls)
;


# Pandas
import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    df = ( person
          .assign(country_code=person['phone_number'].str[:3])
          .merge(country, how='inner', on='country_code')[['id','name_y']]
          .rename(columns={'name_y': 'country'})
         )
    df1 = ( pd.concat(
                [
                  calls[['caller_id','duration']].rename(columns={'caller_id': 'id'}),
                  calls[['callee_id','duration']].rename(columns={'callee_id': 'id'})
                ]
            )
          )
    global_avg = df1['duration'].mean()
    df2 = ( df1
           .merge(df, how='inner', on='id')
           .groupby('country', as_index=0)['duration']
           .mean()
          )
    return df2[df2['duration'] > global_avg][['country']]

