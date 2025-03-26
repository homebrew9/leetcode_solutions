-- Oracle
/* Write your PL/SQL query statement below */
with t (user_id, friend_id) as (
    select user1_id, user2_id from friendship
    union
    select user2_id, user1_id from friendship
)
select f.user1_id, f.user2_id,
       count(*) as common_friend
from friendship f
     inner join t t1 on (t1.user_id = f.user1_id)
     inner join t t2 on (t2.user_id = f.user2_id and t2.friend_id = t1.friend_id)
group by f.user1_id, f.user2_id
having count(*) >= 3
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
with t (user_id, friend_id) as (
    select user1_id, user2_id from friendship
    union
    select user2_id, user1_id from friendship
)
select f.user1_id, f.user2_id,
       count(*) as common_friend
from friendship f
     inner join t t1 on (t1.user_id = f.user1_id)
     inner join t t2 on (t2.user_id = f.user2_id and t2.friend_id = t1.friend_id)
group by f.user1_id, f.user2_id
having count(*) >= 3
;


-- SQL Server
/* Write your T-SQL query statement below */
with t (user_id, friend_id) as (
    select user1_id, user2_id from friendship
    union
    select user2_id, user1_id from friendship
)
select f.user1_id, f.user2_id,
       count(*) as common_friend
from friendship f
     inner join t t1 on (t1.user_id = f.user1_id)
     inner join t t2 on (t2.user_id = f.user2_id and t2.friend_id = t1.friend_id)
group by f.user1_id, f.user2_id
having count(*) >= 3
;


# MySQL
# Write your MySQL query statement below
with t (user_id, friend_id) as (
    select user1_id, user2_id from friendship
    union
    select user2_id, user1_id from friendship
)
select f.user1_id, f.user2_id,
       count(*) as common_friend
from friendship f
     inner join t t1 on (t1.user_id = f.user1_id)
     inner join t t2 on (t2.user_id = f.user2_id and t2.friend_id = t1.friend_id)
group by f.user1_id, f.user2_id
having count(*) >= 3
;


# Pandas
import pandas as pd

def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:
    df = ( pd
          .concat([friendship, friendship[['user2_id','user1_id']]
          .rename(columns={'user2_id':'user1_id', 'user1_id':'user2_id'})])
          .sort_values(['user1_id','user2_id'])
          .reset_index(drop=True)
         )
    return ( friendship
            .merge(df, how='inner', on='user1_id')
            .rename(columns={'user2_id_y':'friend_of_user1', 'user2_id_x': 'user2_id'})
            .merge(df, how='inner', on='user2_id')
            .query('user1_id_y == friend_of_user1')
            .rename(columns={'user1_id_y':'friend_of_user2', 'user1_id_x': 'user1_id'})
            .groupby(['user1_id', 'user2_id'], as_index=0)['friend_of_user1']
            .count()
            .query('friend_of_user1 >= 3')
            .rename(columns={'friend_of_user1': 'common_friend'})
           )

