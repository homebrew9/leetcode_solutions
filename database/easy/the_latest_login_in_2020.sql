-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select user_id, time_stamp,
           dense_rank() over (partition by user_id order by time_stamp desc) as drnk
      from logins
     where to_char(time_stamp, 'yyyy') = '2020'
)
select user_id, time_stamp as last_stamp
  from t
 where drnk = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t as (
    select user_id, time_stamp,
           dense_rank() over (partition by user_id order by time_stamp desc) as drnk
      from logins
     where to_char(time_stamp, 'yyyy') = '2020'
)
select user_id, time_stamp as last_stamp
  from t
 where drnk = 1
;


-- SQL Server
/* Write your T-SQL query statement below */
with t as (
    select user_id, time_stamp,
           dense_rank() over (partition by user_id order by time_stamp desc) as drnk
      from logins
     where YEAR(time_stamp) = 2020
)
select user_id, time_stamp as last_stamp
  from t
 where drnk = 1
;


# MySQL
# Write your MySQL query statement below
with t as (
    select user_id, time_stamp,
           dense_rank() over (partition by user_id order by time_stamp desc) as drnk
      from logins
     where YEAR(time_stamp) = 2020
)
select user_id, time_stamp as last_stamp
  from t
 where drnk = 1
;


# Pandas
import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    df = ( logins[logins['time_stamp'].dt.strftime('%Y')=='2020']
          .rename(columns={'time_stamp': 'last_stamp'})
         )
    return ( df
            .assign(rnk = ( df
                           .groupby('user_id',as_index=0)['last_stamp']
                           .rank(method='max', ascending=0)
                          )
                   )
            .query('rnk == 1')[['user_id','last_stamp']]
           )

