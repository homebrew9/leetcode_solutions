-- Oracle
/* Write your PL/SQL query statement below */
-- "user" is a keyword.
with t (total_users) as (
select count(*) as total_users
from (select distinct user1 from friends union select distinct user2 from friends)
),
t1 (user1, friend_count) as (
select x.user1, count(*) as friend_count
from (
    select user1 as user1, user2 from friends
    union
    select user2 as user1, user1 from friends
) x
group by x.user1
)
select t1.user1, round((t1.friend_count / t.total_users) * 100, 2) as percentage_popularity
from t1
     cross join t
order by t1.user1
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
-- "user" is a keyword.
with t (total_users) as (
select count(*) as total_users
from (select distinct user1 from friends union select distinct user2 from friends)
),
t1 (user1, friend_count) as (
select x.user1, count(*) as friend_count
from (
    select user1 as user1, user2 from friends
    union
    select user2 as user1, user1 from friends
) x
group by x.user1
)
select t1.user1, round((t1.friend_count::numeric / t.total_users::numeric) * 100, 2) as percentage_popularity
from t1
     cross join t
order by t1.user1
;


-- SQL Server
/* Write your T-SQL query statement below */
-- "user" is a keyword.
with t (total_users) as (
select count(*) as total_users
from (select distinct user1 from friends union select distinct user2 from friends) x
),
t1 (user1, friend_count) as (
select x.user1, count(*) as friend_count
from (
    select user1 as user1, user2 from friends
    union
    select user2 as user1, user1 from friends
) x
group by x.user1
)
select t1.user1,
       round(convert(float, t1.friend_count) / convert(float, t.total_users) * 100, 2) as percentage_popularity
from t1
     cross join t
order by t1.user1
;


# MySQL
# Write your MySQL query statement below
-- "user" is a keyword.
with t (total_users) as (
select count(*) as total_users
from (select distinct user1 from friends union select distinct user2 from friends) x
),
t1 (user1, friend_count) as (
select x.user1, count(*) as friend_count
from (
    select user1 as user1, user2 from friends
    union
    select user2 as user1, user1 from friends
) x
group by x.user1
)
select t1.user1,
       round(t1.friend_count / t.total_users * 100, 2) as percentage_popularity
from t1
     cross join t
order by t1.user1
;


# Pandas
import pandas as pd

def popularity_percentage(friends: pd.DataFrame) -> pd.DataFrame:
    # pd.concat([ df[[x, y]] , df[[y, x]] ]) <== does not work unless the columns are renamed!!!
    total_users = len(pd.concat([friends.rename(columns={'user1':'x'})[['x']],
                                 friends.rename(columns={'user2':'x'})[['x']]
                                ]
                               ).drop_duplicates()
                     )
    df = ( pd
          .concat([friends.rename(columns={'user1':'x','user2':'y'}),
                   friends.rename(columns={'user1':'y','user2':'x'})]
                 )
          .drop_duplicates()
          .groupby('x',as_index=False)['y']
          .count()
         )
    df['percentage_popularity'] = round(df['y']/total_users*100, 2)
    return df.rename(columns={'x': 'user1'})[['user1', 'percentage_popularity']].sort_values('user1')

