-- Oracle
/* Write your PL/SQL query statement below */
select query_name,
       round(sum(rating/position) / count(*), 2) as quality,
       round(sum(case when rating < 3 then 1 else 0 end)/count(*) * 100, 2) as poor_query_percentage
from queries
group by query_name
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select query_name,
       round(avg(rating / position::numeric), 2) as quality,
       round(sum(case when rating < 3 then 1 else 0 end) / count(*)::numeric * 100, 2) as poor_query_percentage
  from queries
 group by query_name
;


-- SQL Server
/* Write your T-SQL query statement below */
select query_name,
       round(avg(rating / convert(float, position)), 2) as quality,
       round(sum(case when rating < 3 then 1 else 0 end) / convert(float, count(*)) * 100, 2) as poor_query_percentage
  from queries
 group by query_name
;


# MySQL
# Write your MySQL query statement below
select query_name,
       round(avg(rating / position), 2) as quality,
       round(sum(case when rating < 3 then 1 else 0 end) / count(*) * 100, 2) as poor_query_percentage
  from queries
 group by query_name
;


# Pandas
import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    # Python implements "Banker's rounding" or "rounding to even". For example, round(0.125, 2) = 0.12.
    # So it is best to use a custom rounding function.
    df = ( queries
          .assign(quality=queries['rating']/queries['position'], poor_query_percentage=np.where(queries['rating'] < 3, 1, 0))
          .groupby('query_name', as_index=0)
          .agg(quality=('quality', 'mean'), poor_query_percentage=('poor_query_percentage', 'sum'), count=('query_name', 'count'))
         )
    df['poor_query_percentage'] = (df['poor_query_percentage']/df['count'] * 100).apply(lambda x: int(x * 100 + 0.5) / 100)
    df['quality'] = df['quality'].apply(lambda x: int(x * 100 + 0.5) / 100)
    return df[['query_name', 'quality', 'poor_query_percentage']]

