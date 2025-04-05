-- Oracle
/* Write your PL/SQL query statement below */
with t as (
    select user1_id, user2_id
      from friendship
     where user1_id = 1 or user2_id = 1
),
friends (user_id) as (
    select user_id from (
        select user1_id as user_id from t union
        select user2_id from t
    )
    minus
    select 1 as user_id from dual
)
select distinct page_id as recommended_page
  from likes l
       inner join friends f on (f.user_id = l.user_id)
minus
select page_id from likes where user_id = 1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (friend_id) as (
    select user2_id from friendship where user1_id = 1
    union
    select user1_id from friendship where user2_id = 1
)
select distinct page_id as recommended_page
  from likes
 where user_id in (select friend_id from t)
   and page_id not in (select page_id from likes where user_id = 1)
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (friend_id) as (
    select user2_id from friendship where user1_id = 1
    union
    select user1_id from friendship where user2_id = 1
)
select distinct page_id as recommended_page
  from likes
 where user_id in (select friend_id from t)
   and page_id not in (select page_id from likes where user_id = 1)
;


# MySQL
# Write your MySQL query statement below
with t (friend_id) as (
    select user2_id from friendship where user1_id = 1
    union
    select user1_id from friendship where user2_id = 1
)
select distinct page_id as recommended_page
  from likes
 where user_id in (select friend_id from t)
   and page_id not in (select page_id from likes where user_id = 1)
;


# Pandas
import pandas as pd

def page_recommendations(friendship: pd.DataFrame, likes: pd.DataFrame) -> pd.DataFrame:
    df1 = friendship[friendship['user1_id']==1][['user2_id']].rename(columns={'user2_id':'user_id'})
    df2 = friendship[friendship['user2_id']==1][['user1_id']].rename(columns={'user1_id':'user_id'})
    df3 = pd.concat([df1,df2])
    df = likes.merge(df3, how='inner', on='user_id')[['page_id']].drop_duplicates()
    user1_likes = likes[likes['user_id']==1]['page_id']
    return df[~df['page_id'].isin(user1_likes)].rename(columns={'page_id':'recommended_page'})

