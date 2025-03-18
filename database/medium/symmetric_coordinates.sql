-- Oracle
/* Write your PL/SQL query statement below */
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y from t1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y
  from t1
 order by x, y
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y
  from t1
 order by x, y
;


# MySQL
# Write your MySQL query statement below
with t (x1, y1, x2, y2) as (
    select c1.x as x1, c1.y as y1,
           c2.x as x2, c2.y as y2
    from coordinates c1
         inner join coordinates c2 on (c1.x = c2.y and c2.x = c1.y)
),
t1 (x, y) as (
    select x, y
      from coordinates
     where x = y
     group by x, y
    having count(*) > 1
)
select x1  as x, y1 as y
  from t
 where x1 < y1
union
select x, y
  from t1
 order by x, y
;


# Pandas
import pandas as pd

def symmetric_pairs(coordinates: pd.DataFrame) -> pd.DataFrame:
    df1 = ( coordinates
           .merge(coordinates, how='inner', left_on=['X','Y'], right_on=['Y','X'])
           .query('X_x < Y_x')[['X_x','Y_x']]
           .drop_duplicates()
           .rename(columns={'X_x':'X','Y_x':'Y'})
          )
    df2 = ( coordinates[coordinates['X']==coordinates['Y']]
           .groupby(['X','Y'],as_index=False)
           .agg(cnt=('X','count'))
           .query('cnt > 1')[['X','Y']]
          )
    return pd.concat([df1, df2]).sort_values(['X','Y'])

