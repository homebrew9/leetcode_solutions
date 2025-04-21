-- Oracle
/* Write your PL/SQL query statement below */
select user_id, count(*) as "followers_count"
from followers
group by user_id
order by user_id
;


-- PostgreSQL
-- Write your PostgreSQL query statement below
select user_id, count(*) as followers_count
  from followers
 group by user_id
 order by user_id
;


-- SQL Server
/* Write your T-SQL query statement below */
select user_id, count(*) as followers_count
  from followers
 group by user_id
 order by user_id
;


# MySQL
# Write your MySQL query statement below
select user_id, count(*) as followers_count
from followers
group by user_id
order by user_id
;


# Pandas
# Solution 1
import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return ( followers
            .groupby('user_id', as_index=0)
            .agg(followers_count=('follower_id','count'))
            .sort_values('user_id')
           )

# Solution 2
import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return ( followers
            .groupby('user_id', as_index=0)
            .size()
            .rename(columns={'size':'followers_count'})
            .sort_values('user_id')
           )


