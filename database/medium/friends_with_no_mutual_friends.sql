-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id1, user_id2) as (
    select distinct user_id1, user_id2 from (
        select user_id1, user_id2 from friends
        union all
        select user_id2, user_id1 from friends
    )
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id1, user_id2) as (
    select distinct user_id1, user_id2 from (
        select user_id1, user_id2 from friends
        union all
        select user_id2, user_id1 from friends
    )
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id1, user_id2) as (
    select distinct x.user_id1, x.user_id2
      from (
                select user_id1, user_id2 from friends
                union all
                select user_id2, user_id1 from friends
           ) as x
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


# MySQL
# Write your MySQL query statement below
with t (user_id1, user_id2) as (
    select distinct x.user_id1, x.user_id2
      from (
                select user_id1, user_id2 from friends
                union all
                select user_id2, user_id1 from friends
           ) as x
)
select f1.user_id1, f1.user_id2
from friends f1
where not exists (
    select t.user_id2 from t where t.user_id1 = f1.user_id1
    intersect
    select t.user_id2 from t where t.user_id1 = f1.user_id2
)
order by f1.user_id1, f1.user_id2
;


# Pandas
import pandas as pd

def friends_with_no_mutual_friends(friends: pd.DataFrame) -> pd.DataFrame:
    df = (pd.concat(
                     [friends[['user_id1','user_id2']].rename(columns={'user_id1':'id1', 'user_id2':'id2'}),
                      friends[['user_id2','user_id1']].rename(columns={'user_id2':'id1', 'user_id1':'id2'})
                     ]
                   )
         )
    df1 = ( friends
           .merge(df, how='inner', left_on='user_id1', right_on='id1')
           .merge(df, how='inner', left_on='user_id2', right_on='id2')
           .query('id2_x == id1_y')
          )
    return ( friends
            .merge(df1, how='left', on=['user_id1','user_id2'])
            .query('id1_x.isna()')[['user_id1','user_id2']]
            .sort_values(['user_id1','user_id2'])
           )

